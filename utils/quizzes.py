import json

from .quiz import Quiz

class Quizzes:
    def __init__(self):
        self.quizzes = json.load(open('data/quizzes.json'))

    def get_quiz(self, quiz_name):
        for quiz in self.quizzes:
            if quiz['name'] == quiz_name:
                return Quiz(quiz)

    def get_quizzes(self):
        return [ Quiz(quiz) for quiz in self.quizzes ]

    def create_quiz(self, quiz_name, questions):
        try:
            for quiz in self.quizzes:
                if quiz['name'] == quiz_name:
                    return False

            quiz_json = {'name': quiz_name, 'questions': [ question.to_json() for question in questions ]}
            self.quizzes.append(quiz_json)
            self.save_json()

            return Quiz(quiz_json)
        except Exception as e:
            print(e)
            return False

    def delete_quiz(self, quiz_name):
        for quiz in self.quizzes:
            if quiz['name'] == quiz_name:
                self.quizzes.remove(quiz)

    def save_json(self):
        json.dump(self.quizzes, open('data/quizzes.json', 'w'))
