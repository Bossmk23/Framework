# main.py

# These imports are needed to trigger registration
import models.simple_model
import datasets.dummy_dataset
import trainers.base_trainers

from utils.loader import load_config, initialize_component

def main():
    config = load_config("configs/base_configs.yaml")

    model = initialize_component("model", config["model"])
    dataset = initialize_component("dataset", config["dataset"])
    trainer = initialize_component("trainer", config["trainer"])

    model.summary()
    trainer.train(model, dataset)

if __name__ == "__main__":
    main()
