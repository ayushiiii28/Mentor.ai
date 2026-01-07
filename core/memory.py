class SimpleMemory:
    def __init__(self):
        self.history = []

    def add(self, text: str):
        self.history.append(text)

    def get_last(self, n=5):
        return self.history[-n:]
