import os
import shutil
import click
import platform
import subprocess

from .common.project_structure import PROJECT_STRUCTURE
from .common.framework_requirements import FRAMEWORK_REQUIREMENTS

@click.group()
def cli():
    """MLProject command line interface."""
    pass

@cli.command()
@click.argument("project_name", required=False, default=".")
@click.option("--framework", type=click.Choice(["tensorflow", "keras", "torch"]), default=None,
              help="Framework to include in requirements.txt")
@click.option("--install", is_flag=True, help="Automatically install dependencies after creating requirements.txt")
def init(project_name, framework, install):
    """Initialize a new ML project with standard folders and optional framework."""
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

    if framework:
        if framework in FRAMEWORK_REQUIREMENTS:
            framework_pkgs = FRAMEWORK_REQUIREMENTS[framework].get(os_type)
            if framework == "torch" and os_type == "darwin":
                # Special case: torch on macOS
                special_command = (
                    "pip3 install --pre torch torchvision torchaudio "
                    "--extra-index-url https://download.pytorch.org/whl/nightly/cpu"
                )
                click.echo("PyTorch on macOS requires a special install command. "
                           "It will not be written to requirements.txt.")
            elif framework_pkgs:
                base_requirements.extend(framework_pkgs)
            else:
                click.echo(f"Framework {framework} not supported on {os_type}, skipping...")
        else:
            click.echo(f"Unknown framework: {framework}")

    with open(req_path, "w") as f:
        f.write("\n".join(base_requirements) + "\n")

    click.echo(f"requirements.txt created with {framework or 'base'} dependencies")

    # Auto-install if requested
    if install:
        click.echo("Installing dependencies...")
        subprocess.check_call(["pip", "install", "-r", req_path])
        if special_command:
            click.echo(f"⚡ Running special install for PyTorch on macOS:\n   {special_command}")
            subprocess.check_call(special_command, shell=True)

    click.echo(f"\nProject '{project_name}' structure created at {root} with {framework}")


@cli.command()
@click.argument("project_name", required=False, default=".")
def clear(project_name):
    """Clear all project folders"""
    root = os.path.abspath(project_name)

    click.confirm(
        f"This will DELETE all project folders under {root}. Continue?",
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
