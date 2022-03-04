class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def check_answer(self, answer):
        return answer == self.correct_answer

    def to_json(self):
        return {
            'question': self.question,
            'answers': self.answers,
            'correct_answer': self.correct_answer
        }