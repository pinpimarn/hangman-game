class VocabContainer:
    def __init__(self, container = []):
        self.container = container

    def add_word(self, vocab): #times = จำนวนการเล่น
        self.container.append(vocab)
