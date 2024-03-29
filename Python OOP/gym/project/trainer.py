class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer.id += 1
        return Trainer.id - 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
