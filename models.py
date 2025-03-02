class Question:
    def __init__(self, destination, clues, fun_fact, options, correct_answer):
        self.destination = destination
        self.clues = clues
        self.fun_fact = fun_fact
        self.options = options
        self.correct_answer = correct_answer

    def to_dict(self):
        return self.__dict__
