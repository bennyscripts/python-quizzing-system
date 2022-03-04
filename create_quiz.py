from utils.quizzes import Quizzes
from utils.question import Question

def main():
    quizzes = Quizzes()
    quiz = {}

    quiz['name'] = input("Enter quiz name: ")
    quiz['questions'] = []

    while True:
        question = Question("", [], "")
        
        question.question = input("Enter question: ")
        question.answers = input("Enter answers (separated by comma): ").split(',')
        question.correct_answer = input("Enter the correct answer: ")

        quiz['questions'].append(question)

        more = input("Add another question? (y/n) ")
        if more.lower() == 'n':
            break

    quizzes.create_quiz(quiz['name'], quiz['questions'])

    print("Quiz created!")

if __name__ == '__main__':
    main()