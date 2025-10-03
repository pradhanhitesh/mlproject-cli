# mlproject-cli

`mlproject` is a lightweight Python package + CLI tool for bootstrapping Machine Learning project structures. It helps you quickly scaffold standard folders like `config/`, `src/`, `experiments/`, and `tests/` so you can focus on your code instead of boilerplate setup.

## 🚀 Features

- Scaffold a clean ML project structure with one command
- Includes `config.yml` in `config/` by default
- Creates a `src/` package with subfolders for:
  - `models/`
  - `data/`
  - `inference/`
  - `preproc/`
  - `train/`
  - `utils/`
- Provides `clear` command to safely remove all project folders
- Works with both pip/venv and conda environments
