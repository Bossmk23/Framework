from registry import register

@register("dataset", "dummy_dataset")
class DummyDataset:
    def __init__(self, num_samples, input_size):
        self.data = [[0] * input_size for _ in range(num_samples)]
        print(f"[Dataset] Loaded {num_samples} samples")
