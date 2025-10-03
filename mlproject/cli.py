import os
import shutil
import click

from .common.logic import create, delete, download

@click.group()
def cli():
    """MLProject CLI: Build quick and modular ML project scaffolding"""
    pass

# --------------------
# CREATE PROJECT COMMAND
# --------------------
@cli.command()
@click.argument("project_name", required=False, default=".")
@click.option(
    "--framework",
    type=click.Choice(["tensorflow", "keras", "torch"]),
    default=None,
    help="Framework to include in requirements.txt",
)
@click.option(
    "--install",
    is_flag=True,
    help="Automatically install dependencies after creating requirements.txt",
)
def init(project_name, framework, install):
    """Initialize a new MLProject"""
    create(project_name, framework, install)

# --------------------
# CLEAR PROJECT COMMAND
# --------------------
@cli.command()
@click.argument("project_name", required=False, default=".")
def clear(project_name):
    """Clear all project folders"""
    delete(project_name)

# --------------------
# DATASET DOWNLOAD COMMAND
# --------------------
@cli.command(name="download-dataset")
@click.option(
    "--source",
    type=click.Choice(["kaggle"]),
    required=True,
    help="Source to download the dataset from",
)
@click.option(
    "-i", "--identifier",
    required=True,
    help="Dataset identifier (e.g., 'username/dataset')"
)
@click.option(
    "-o", "--output",
    required=True,
    help="Path to save the dataset"
)
def download_dataset(source, identifier, output):
    """Download datasets from supported sources (currently Kaggle)."""
    download(identifier, source, output)
