from .question import Question

class Quiz:
    def __init__(self, quiz_json):
        self.quiz_json = quiz_json
        self.name = quiz_json['name']
        self.questions = [ Question(question_json["question"], question_json["answers"], question_json["correct_answer"]) for question_json in quiz_json['questions'] ]