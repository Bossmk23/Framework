from registry import register

@register("model", "simple_model")
class SimpleModel:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

    def summary(self):
        print(f"[Model] SimpleModel with input={self.input_size}, output={self.output_size}")
