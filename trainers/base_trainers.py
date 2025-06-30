from registry import register

@register("trainer", "base_trainer")
class BaseTrainer:
    def __init__(self, epochs, learning_rate):
        self.epochs = epochs
        self.learning_rate = learning_rate

    def train(self, model, dataset):
        print(f"[Trainer] Training for {self.epochs} epochs with lr={self.learning_rate}")
        for i in range(self.epochs):
            print(f"[Trainer] Epoch {i+1}: Training on {len(dataset.data)} samples")
        print("[Trainer] Done.")
