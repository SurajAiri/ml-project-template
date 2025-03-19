# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Getting Started

### Prerequisites

- Python {{ cookiecutter.python_version }}
- {{ cookiecutter.package_manager }} (package manager)

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd {{ cookiecutter.repo_name }}
```

2. Set up the Python environment:
```bash
{% if cookiecutter.package_manager == 'uv' %}
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
{% elif cookiecutter.package_manager == 'conda' %}
conda env create -f environment.yml
conda activate {{ cookiecutter.repo_name }}
{% else %}
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
{% endif %}
```

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-sa-initial-data-exploration`.
    │
    ├── pyproject.toml     <- The requirements file for reproducing the analysis environment
    │
    ├── {{ cookiecutter.repo_name }}  <- Source code for use in this project.
    │   ├── __init__.py    <- Makes {{ cookiecutter.repo_name }} a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── models         <- Scripts to train models and make predictions
    │   │
    │   └── utils          <- Utility functions
    │
    └── tests              <- Test files

## License

This project is licensed under the {{ cookiecutter.license }} License - see the LICENSE file for details.

## Author

{{ cookiecutter.author_name }} - {{ cookiecutter.email }}