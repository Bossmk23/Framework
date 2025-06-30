# Contributing Guide

Thank you for considering a contribution to the Custom AI Training Framework.  
These guidelines explain the workflow, code style and naming rules that keep the project easy to understand and extend.

---

## 1 Before you start

1. **Open an issue** describing the change you plan to make.  
   This prevents duplicated effort and allows discussion.
2. **Fork** the repository and create a feature branch:  
   `git checkout -b feat/my-new-component`.

---

## 2 Code style

* Follow **PEP 8** for Python.
* Write short, descriptive doc‑strings for every public class and method.
* Use `black` or another formatter if you prefer, but stay consistent.

---

## 3 Folder and file naming

| Folder       | Contents                          | Naming pattern                 |
|--------------|-----------------------------------|--------------------------------|
| `core/`      | Abstract base classes             | `base_*.py`                    |
| `models/`    | Concrete model classes            | `*_model.py`                   |
| `datasets/`  | Dataset loader classes            | `*_dataset.py`                 |
| `trainers/`  | Training loop implementations     | `*_trainer.py`                 |
| `utils/`     | Helper scripts (logger, loader…)  | descriptive (`logger.py`)      |
| `configs/`   | YAML experiment files             | `*.yaml`                       |

All folders that contain Python code **must** include an `__init__.py` file (can be empty).

---

## 4 Adding a new model, dataset or trainer

1. Create a new file in the correct folder (see table above).
2. Subclass the matching abstract base class from `core/`.
3. Register the class with the decorator from `registry.py`.

   ```python
   from registry import register
   from core.base_model import BaseModel

   @register("model", "my_model")
   class MyModel(BaseModel):
       ...
   ```

4. Update or create a YAML file under `configs/` to reference your new component.

   ```yaml
   model:
     name: my_model
     params:
       ...
   ```
5. Run a quick test:

   ```bash
   python main.py --config configs/your_config.yaml
   ```

---

## 5 Running unit or smoke tests

For simple checks:

```bash
python -m pytest                 # if tests are added
python main.py                   # quick end‑to‑end run
python train.py --epochs 1       # logger / TensorBoard check
```

---

## 6 Commit and pull‑request workflow

1. **Commit often**, but keep messages meaningful:
   ```
   git commit -m "Add MyModel with registration"
   ```
2. **Push** your branch and open a pull request (PR) on GitHub.
3. Reference the issue number in the PR description.
4. A maintainer will review your code.  
   Address any feedback and push additional commits to the same branch.
5. Once approved, the PR will be merged into `main`.

---

## 7 Issue reporting

When filing a bug report, include:

* Steps to reproduce the error
* Python version and OS
* Stack trace or error message
* Any relevant config or command‑line parameters

Clear reports help us fix issues faster.

---

## 8 Code of conduct

Be respectful and constructive.  
We welcome suggestions and improvements, but personal attacks or disrespectful language will not be tolerated.

---

Thank you for helping improve the Custom AI Training Framework.
