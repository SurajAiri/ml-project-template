from pathlib import Path

def create_project_structure(base_dir: Path):
    directories = [
        "{{cookiecutter.project_name}}/data/raw",
        "{{cookiecutter.project_name}}/data/processed",
        "{{cookiecutter.project_name}}/data/external",
        "{{cookiecutter.project_name}}/notebooks/exploratory",
        "{{cookiecutter.project_name}}/notebooks/modeling",
        "{{cookiecutter.project_name}}/notebooks/evaluation",
        "{{cookiecutter.project_name}}/src/data",
        "{{cookiecutter.project_name}}/src/features",
        "{{cookiecutter.project_name}}/src/models",
        "{{cookiecutter.project_name}}/src/utils",
        "{{cookiecutter.project_name}}/src/pipelines",
        "{{cookiecutter.project_name}}/tests",
        "{{cookiecutter.project_name}}/artifacts/checkpoints",
        "{{cookiecutter.project_name}}/artifacts/models",
        "{{cookiecutter.project_name}}/artifacts/logs",
        "{{cookiecutter.project_name}}/configs",
        "{{cookiecutter.project_name}}/reports/figures",
        "{{cookiecutter.project_name}}/scripts",
    ]
    
    files = {
        "{{cookiecutter.project_name}}/src/__init__.py": "",
        "{{cookiecutter.project_name}}/src/data/load_data.py": "# Load data script",
        "{{cookiecutter.project_name}}/src/data/preprocess.py": "# Preprocessing script",
        "{{cookiecutter.project_name}}/src/models/train.py": "# Training script",
        "{{cookiecutter.project_name}}/src/models/evaluate.py": "# Evaluation script",
        "{{cookiecutter.project_name}}/tests/test_data.py": "# Test data loading",
        "{{cookiecutter.project_name}}/tests/test_features.py": "# Test feature engineering",
        "{{cookiecutter.project_name}}/tests/test_models.py": "# Test model pipeline",
        "{{cookiecutter.project_name}}/configs/data_config.yaml": "# Data config",
        "{{cookiecutter.project_name}}/configs/model_config.yaml": "# Model config",
        "{{cookiecutter.project_name}}/configs/pipeline_config.yaml": "# Pipeline config",
        "{{cookiecutter.project_name}}/reports/results.csv": "",
        "{{cookiecutter.project_name}}/reports/summary.md": "# Project Summary",
        "{{cookiecutter.project_name}}/scripts/run_pipeline.py": "# Run ML pipeline",
        "{{cookiecutter.project_name}}/scripts/serve_model.py": "# Serve model API",
        "{{cookiecutter.project_name}}/scripts/train_model.py": "# Train model script",
        "{{cookiecutter.project_name}}/pyproject.toml": "# Project dependencies",
        "{{cookiecutter.project_name}}/poetry.lock": "",
        "{{cookiecutter.project_name}}/Dockerfile": "# Dockerfile",
        "{{cookiecutter.project_name}}/.gitignore": "__pycache__/\n*.pyc\n*.pyo\n*.env\n",
        "{{cookiecutter.project_name}}/README.md": "# {{cookiecutter.project_name}}",
    }
    
    for directory in directories:
        dir_path = base_dir / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        (dir_path / ".gitkeep").touch()
    
    for file, content in files.items():
        file_path = base_dir / file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding='utf-8')

if __name__ == "__main__":
    base_path = Path(".")
    create_project_structure(base_path)
