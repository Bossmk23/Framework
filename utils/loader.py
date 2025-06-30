import yaml
from registry import get_component

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def initialize_component(category, config):
    cls = get_component(category, config["name"])
    return cls(**config.get("params", {}))
