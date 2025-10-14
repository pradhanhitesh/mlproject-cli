# mlproject

`mlproject` is a lightweight Python package + CLI tool for bootstrapping Machine Learning (ML) project structures. It helps you quickly scaffold standard folders like `config/`, `src/`, `experiments/`, and `notebooks/` so you can focus on your code instead of boilerplate setup.

You can view this projects built using `mlproject-cli`: [Diabetic Retinopathy - Predicting risk of macular edema using OCT images](https://github.com/pradhanhitesh/diabetic-retinopathy-kaggle)

## Features

* Scaffold a clean ML project structure with one command
* Includes `config.yml` in `config/` by default
* Creates a `src/` package with subfolders for modular development
* Provides `clear` command to safely remove all project folders
* Works with both pip/venv and conda environments

## Scaffold

When you run `mlproject init your-project-name`, it creates the following structure:

```
your-project-name/
│
├── config/
│   └── config.yml        
│
├── experiments/          
│
├── notebooks/            
│
├── src/                  
│   ├── __init__.py
│   ├── models/          
│   ├── data/             
│   ├── inference/        
│   ├── preproc/         
│   ├── train/            
│   ├── test/             
│   ├── utils/            
│   └── logs/             
│
└── README.md             
```

## Folder Description

This is a standard description of the folders which are created upon `mlproject` initialization.

* **`config/`** → Store project-wide configuration files (e.g., `config.yml` with hyperparameters, paths).
* **`experiments/`** → Save experiment runs, metadata, results, or checkpoints.
* **`notebooks/`** → Keep exploratory Jupyter notebooks, EDA, and rapid prototyping code.
* **`src/models/`** → Define ML/DL model architectures (e.g., PyTorch `nn.Module`, TensorFlow models).
* **`src/data/`** → Data loading scripts, dataset definitions, preprocessing pipelines.
* **`src/inference/`** → Scripts for running inference, model serving, or batch predictions.
* **`src/preproc/`** → Feature engineering, normalization, tokenization, or other preprocessing utilities.
* **`src/train/`** → Training code, loss functions, optimizers, callbacks, experiment runners.
* **`src/test/`** → Testing and evaluation scripts, unit tests, and benchmarking.
* **`src/utils/`** → Shared helper functions, logging setup, config readers, small utilities.
* **`src/logs/`** → Training and inference logs, tensorboard outputs, debug files.

## Installation

You can install `mlproject` directly from source or package index.

### Requirements

* Python **3.8+**
* Virtual environment (recommended):

  ```bash
  python3 -m venv venv
  source venv/bin/activate   # On Linux/Mac
  venv\Scripts\activate      # On Windows
  ```


### From Release (latest development version)

```bash
pip install https://github.com/pradhanhitesh/mlproject-cli/releases/download/v0.4.4/mlproject-0.4.4-py3-none-any.whl
```

### From Source (latest development version)

```bash
git clone https://github.com/pradhanitesh/mlproject-cli.git
cd mlproject-cli
pip install -e .
```

## Usage

### 1. Initialize a New Project

Scaffold a fresh ML project structure:

```bash
mlproject init your-project-name
```

This creates the full folder structure under `your-project-name/`. But this will not install any ML framework. If you want to install any particular framework, see following options which needs to be specified during project initialization.

#### Options:

* **`--framework`** → Add framework-specific dependencies (`tensorflow`, `keras`, `torch`) into `requirements.txt`.
* **`--install`** → Automatically install dependencies after creating `requirements.txt`.

Example:

```bash
mlproject init your-project-name --framework torch --install
```
This will initialize project folder `your-project-name` and also install `torch` library in your local `env`. If you forget to add `--install` tag, the command will only generate `requirement.txt` file within your `your-project-name` folder.

---

### 2. Clear Project Structure

Remove scaffolded project folders from the current directory (⚠️ destructive):

```bash
mlproject clear
```

Or specify a project folder to clear:

```bash
mlproject clear your-project-name
```

---

### 3. Download Dataset

Download datasets directly into your project (currently supports **Kaggle**).

```bash
mlproject download-dataset --source kaggle -i username/dataset -o your-project-name/data
```

#### Arguments:

* **`--source`** → Dataset source (currently only `kaggle`).
* **`-i, --identifier`** → Dataset identifier (e.g., `zillow/zecon`).
* **`-o, --output`** → Output path to save dataset.

## Contributing

Contributions, issues, and feature requests are welcome!

If you’d like to contribute to `mlproject-cli`, here’s how you can get started:

### 1. Fork & Clone

```bash
git clone https://github.com/pradhanhitesh/mlproject-cli.git
cd mlproject-cli
```

### 2. Set Up Development Environment

Install dependencies in editable/development mode:

```bash
pip install -e ".[dev]"
```

### 3. Make Your Changes

* Follow the existing code style and folder structure.
* Add or update tests under `tests/`.
* Make sure commands (`init`, `clear`, `download-dataset`) are not broken.

### 4. Commit & Push

Use clear commit messages:

```bash
git checkout -b feature/your-feature
git commit -m "feat: add support for XYZ"
git push origin feature/your-feature
```

### 5. Open a Pull Request

Go to your fork on GitHub and submit a **Pull Request** against the `main` branch.

## License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, merge, publish, and distribute this project for personal or commercial use, provided that the copyright notice and this permission notice are included in all copies.

## Thank You

This tool was built to make starting Machine Learning projects **faster, cleaner, and less painful**.
If you find it useful:

* ⭐ Star the repo on GitHub
* 🐛 Open an issue if you spot a bug
* 💡 Suggest improvements or contribute code via PRs

Together, we can make ML development more productive 



