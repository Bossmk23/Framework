from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def forward(self, x):
        pass

    @abstractmethod
    def save(self, path):
        pass

    @abstractmethod
    def load(self, path):
        pass
