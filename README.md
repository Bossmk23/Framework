# Custom AI Training Framework

## 1 What this project is
This repository holds a small but fully‑featured framework for training machine‑learning models in a consistent, reusable way.  
Key design goals:

* **Modular code** Models, datasets and training loops live in their own folders.
* **Config‑driven workflow** A single YAML file chooses which components run.
* **Experiment management** Utilities for logging, seeding, CLI arguments and TensorBoard help you reproduce and track results.
* **Ease of extension** Adding a new model or dataset requires only one Python file and one line in the config.

This project was completed as part of a team-based internship assignment.  
All members contributed to building and organizing the modular AI training framework collaboratively.


---

## 2 Folder overview

```
custom-ai-training-framework/
├── core/          # Abstract base classes
├── models/        # Example and future models
├── datasets/      # Example and future datasets
├── trainers/      # Trainer implementations
├── utils/         # Loader, logger, seed, CLI helpers
├── configs/       # YAML files that pick components
├── docs/          # System diagram or additional docs
├── main.py        # Runs an experiment from YAML
├── train.py       # Stand‑alone demo with logger + TensorBoard
├── README.md
└── CONTRIBUTING.md
```

Every code folder contains an **`__init__.py`** file so that it behaves as a Python package.

---

## 3 Prerequisites

* Python 3.8 or later  
* pip  
* Recommended: virtual environment (`python -m venv venv`)

Install required packages:

```bash
pip install torch torchvision pyyaml tensorboard numpy
```

---

## 4 Running an experiment (config‑based)

1. Open `configs/base_configs.yaml` and adjust the parameters if desired:

   ```yaml
   model:
     name: simple_model
     params:
       input_size: 10
       output_size: 1

   dataset:
     name: dummy_dataset
     params: {}

   trainer:
     name: base_trainer
     params:
       epochs: 5
       learning_rate: 0.01
   ```

2. Launch the framework:

   ```bash
   python main.py
   ```

Behind the scenes `main.py`:

1. Loads the YAML file.
2. Uses `utils/loader.py` to locate the correct class in `registry.py`.
3. Instantiates the model, dataset and trainer with their parameters.
4. Starts training and prints progress.

---

## 5 Running the stand‑alone demo (`train.py`)

`train.py` shows how to combine the logging, seeding and CLI utilities.

```bash
python train.py --experiment_name "demo" --epochs 10 --batch_size 32
```

During execution you will see:

* Timestamped log messages in both console and `logs/`.
* TensorBoard summaries.  
  Start TensorBoard with  
  `tensorboard --logdir logs` and open http://localhost:6006.

---

## 6 How the framework fits together

```
main.py
  └─> load_config()      (utils/loader.py)
        └─> registry.py  (category + name)
              ├─> model class
              ├─> dataset class
              └─> trainer class
  └─> trainer.train(model, dataset)
        └─> logger · seed · CLI args · TensorBoard
```

A detailed diagram is provided in **docs/diagram.png**.

---

## 7 Extending the framework

1. **Create** a new Python file in the correct folder (for example `models/my_model.py`).
2. **Subclass** the relevant base class (`BaseModel`, `BaseDataset`, or `BaseTrainer`).
3. **Register** it with the decorator:

   ```python
   from registry import register
   from core.base_model import BaseModel

   @register("model", "my_model")
   class MyModel(BaseModel):
       ...
   ```

4. **Reference** it in a YAML config:

   ```yaml
   model:
     name: my_model
     params:
       input_size: 32
       output_size: 2
   ```

No changes are required to `main.py` or other framework code.

---

## 8 Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `ModuleNotFoundError` | Missing `__init__.py` | Add an empty `__init__.py` to the folder |
| “KeyError” in `registry` | Component not registered | Confirm the decorator name matches YAML |
| TensorBoard shows no data | Wrong log directory | Use `--log_dir` flag in `train.py` |

---

## 9 License

Specify your chosen license here (MIT, Apache‑2.0, etc.).
