import os
import time

from utils.quizzes import Quizzes

def main():
    os.system('cls')

    quizzes = Quizzes()
    quizzes_list = quizzes.get_quizzes()

    print("Which quiz would you like to play?")
    
    for quiz in quizzes_list:
        print(f"- {quiz.name}")

    selected_quiz = input("\n>> ")

    if selected_quiz in [ quiz.name for quiz in quizzes.get_quizzes() ]:
        quiz = quizzes.get_quiz(selected_quiz)

        print(f"\nYou selected, {selected_quiz}")
        print("Loading quiz...")
        
        time.sleep(2)
        os.system('cls')
        results = []

        for question in quiz.questions:
            print(quiz.name)
            print("-" * len(quiz.name))
            print()

            question_number = quiz.questions.index(question) + 1

            print(f"({question_number}/{len(quiz.questions)}) " + question.question)
            for answer in question.answers:
                print(f"- {answer}")

            selected_answer = input("\n>> ")
            correct = question.check_answer(selected_answer)
            results.append({
                'question': question.question,
                'user_answer': selected_answer,
                'correct_answer': question.correct_answer,
                'correct': correct
            })

            os.system('cls')

        print("Results")
        print("-" * len("Results"))
        print()

        for result in results:
            print(f"{result['question']}")
            print(f"Your answer: {result['user_answer']}")

            if result['correct']:
                print("You got this question correct!")

            else:
                print(f"The correct answer was {result['correct_answer']}")

            print()

        total_correct = sum(result['correct'] for result in results)
        total_questions = len(results)

        print(f"You got {total_correct} out of {total_questions} questions correct!")
        
        play_another_quiz = input("\nPlay another quiz? (Y/n) ")

        if play_another_quiz == 'y':
            main()
            
        else:
            print("Thanks for playing.")

    elif selected_quiz == 'q':
        print("Thanks for playing.")

    else:
        print("Invalid quiz")
        main()

    input("\nPress enter to exit...")

if __name__ == "__main__":
    main()