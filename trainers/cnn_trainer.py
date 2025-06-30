from core.base_trainer import BaseTrainer

class CNNTrainer(BaseTrainer):
    def train(self):
        print("Training CNN model")

    def evaluate(self):
        print("Evaluating model")

    def run(self):
        self.train()
        self.evaluate()
