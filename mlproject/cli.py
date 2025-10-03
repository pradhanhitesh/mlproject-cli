import os
import shutil
import click

# New folder structure
PROJECT_STRUCTURE = {
    "config": ["config.yml"],
    "experiments": [],
    "src": [
        "__init__.py",
        "models/",
        "data/",
        "inference/",
        "preproc/",
        "train/",
        "utils/",
    ],
    "tests": [],
}

@click.group()
def cli():
    """MLProject command line interface."""
    pass

@cli.command()
@click.argument("project_name", required=False, default=".")
def init(project_name):
    """Initialize a new ML project with standard folders."""
    root = os.path.abspath(project_name)
    os.makedirs(root, exist_ok=True)

    for folder, contents in PROJECT_STRUCTURE.items():
        folder_path = os.path.join(root, folder)
        os.makedirs(folder_path, exist_ok=True)

        for item in contents:
            item_path = os.path.join(folder_path, item)
            if item.endswith("/"):  # subfolder
                os.makedirs(item_path, exist_ok=True)
                click.echo(f"Created {item_path}/")
            else:  # file
                if not os.path.exists(item_path):
                    with open(item_path, "w") as f:
                        if item == "config.yml":
                            f.write("# Default configuration\n")
                        elif item == "__init__.py":
                            f.write("# Makes this a Python package\n")
                        else:
                            f.write("")
                    click.echo(f"Created {item_path}")
        click.echo(f"Initialized {folder}/")

    click.echo(f"\n🎉 Project '{project_name}' structure created at {root}")


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
