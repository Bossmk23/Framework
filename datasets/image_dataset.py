from core.base_dataset import BaseDataset

class ImageDataset(BaseDataset):
    def load_data(self):
        print("Loading image data")

    def preprocess(self, data):
        print("Preprocessing data")
