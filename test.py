from utils.quizzes import Quizzes
from utils.question import Question

quizzes = Quizzes()
quiz = quizzes.create_quiz('Example quiz', [
    Question('What is the capital of France?', ['Paris', 'London', 'Berlin', 'Rome'], 'Paris'),
    Question('What is the capital of Germany?', ['Paris', 'London', 'Berlin', 'Rome'], 'Berlin'),
    Question('What is the capital of Italy?', ['Paris', 'London', 'Berlin', 'Rome'], 'Rome')
])