# Python Quizzing System
A quzzing system created in Python.  
Easily create a quiz with multiple questions and answers.  

> ### How to use
> - Download the code as a ZIP.
> - Run `create_quiz.py` to create a quiz.
> - Play your quiz with `play_quiz.py`.

## Playing and creating
> ### Playing a quiz
> Playing a quiz requires a bit more code or by using the `play_quiz` script.  
> The reason why quiz playing feature was not added to the quiz object is because of it limiting the use cases.  
> You can view how I made the quiz playing code in `play_quiz.py`.

> ### Creating a quiz
> You can create a quiz with the `create_quiz` script or by making one in code.  
> Example code to create a quiz is below.  
> ```python
> from utils.quizzes import Quizzes
> from utils.question import Question
> 
> quizzes = Quizzes()
> quiz = quizzes.create_quiz('Example quiz', [
>     Question('What is the capital of France?', ['Paris', 'London', 'Berlin', 'Rome'], 'Paris'),
>     Question('What is the capital of Germany?', ['Paris', 'London', 'Berlin', 'Rome'], 'Berlin'),
>     Question('What is the capital of Italy?', ['Paris', 'London', 'Berlin', 'Rome'], 'Rome')
> ])
> ```