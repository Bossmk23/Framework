from core.base_model import BaseModel

class CNNModel(BaseModel):
    def build(self):
        print("Building CNN model")

    def forward(self, x):
        print("Running inference on", x)

    def save(self, path):
        print("Model saved to", path)

    def load(self, path):
        print("Model loaded from", path)
