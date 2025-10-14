import os
import click
import shutil
import platform
import subprocess
import kagglehub

from .project import PROJECT_STRUCTURE
from .frameworks import FRAMEWORK_REQUIREMENTS

def create(project_name, framework, install):
    """Create a new ML project with standard folders and optional framework."""
    root = os.path.abspath(project_name)
    os.makedirs(root, exist_ok=True)

    # Create project structure
    for folder, contents in PROJECT_STRUCTURE.items():
        folder_path = os.path.join(root, folder)
        os.makedirs(folder_path, exist_ok=True)

        for item in contents:
            item_path = os.path.join(folder_path, item)
            if item.endswith("/"):
                os.makedirs(item_path, exist_ok=True)
                click.echo(f"Created {item_path}/")
            else:
                if not os.path.exists(item_path):
                    with open(item_path, "w") as f:
                        if item == "config.yml":
                            f.write("# Default configuration\n")
                        elif item == "__init__.py":
                            f.write("# Makes this a Python package\n")
                        else:
                            f.write("")
                    click.echo(f"Created {item_path}")
        click.echo(f"Created {folder}/")

    # Create requirements.txt
    req_path = os.path.join(root, "requirements.txt")
    base_requirements = ["numpy", "pandas", "scikit-learn"]

    os_type = platform.system().lower()
    special_command = None
    extra_index_url = None

    if framework:
        if framework in FRAMEWORK_REQUIREMENTS:
            framework_pkgs = FRAMEWORK_REQUIREMENTS[framework].get(os_type)
            if framework == "torch":
                if os_type == "darwin":
                    # Special case: torch on macOS (CPU only)
                    special_command = (
                        "pip3 install --pre torch torchvision torchaudio "
                        "--extra-index-url https://download.pytorch.org/whl/nightly/cpu"
                    )
                    click.echo("PyTorch on macOS requires a special install command. "
                               "It will not be written to requirements.txt.")
                elif os_type == "windows":
                    extra_index_url = "--extra-index-url https://download.pytorch.org/whl/cu121"
                    framework_pkgs = [pkg for pkg in framework_pkgs if not pkg.startswith("--index-url")]
                    base_requirements.extend(framework_pkgs)
                else:
                    base_requirements.extend(framework_pkgs)
            elif framework_pkgs:
                base_requirements.extend(framework_pkgs)
            else:
                click.echo(f"Framework {framework} not supported on {os_type}, skipping...")
        else:
            click.echo(f"Unknown framework: {framework}")

    # Write requirements.txt
    with open(req_path, "w") as f:
        f.write("\n".join(base_requirements) + "\n")
        if extra_index_url:
            f.write(f"{extra_index_url}\n")

    click.echo(f"requirements.txt created with {framework or 'base'} dependencies")

    # Auto-install if requested
    if install:
        click.echo("Installing dependencies...")
        try:
            subprocess.check_call(["pip", "install", "-r", req_path])
        except subprocess.CalledProcessError:
            click.echo("Some dependencies failed to install. Please check your pip or Python version.")
        if special_command:
            click.echo(f"Running special install for PyTorch on macOS:\n   {special_command}")
            subprocess.check_call(special_command, shell=True)

    click.echo(f"\nProject '{project_name}' structure created at {root}")


def delete(project_name):
    """Clear all project folders"""
    root = os.path.abspath(project_name)

    click.confirm(
        f"This will delete all project folders under {root}. Continue?",
        abort=True
    )

    for folder in PROJECT_STRUCTURE.keys():
        folder_path = os.path.join(root, folder)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            click.echo(f"Deleted {folder_path}")
        else:
            click.echo(f"Skipped {folder_path} (not found)")

    click.echo(f"\nProject '{project_name}' cleared.")

def download(identifier, source, output):
    if source == "kaggle":
        click.echo(f"Downloading dataset '{identifier}' from Kaggle...")
        path = kagglehub.dataset_download(str(identifier))

        # Ensure project root exists
        os.makedirs(output, exist_ok=True)

        # Destination folder inside project root
        dest = os.path.join(output, identifier.split("/")[-1])
        os.makedirs(dest, exist_ok=True)

        # Copy dataset contents to project root/datasets/identifier_name
        if os.path.isdir(path):
            for item in os.listdir(path):
                s = os.path.join(path, item)
                d = os.path.join(dest, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
        else:
            shutil.copy2(path, dest)

        click.echo(f"Dataset saved at: {dest}")
        return dest

    else:
        click.echo("Unsupported source")
        return None
