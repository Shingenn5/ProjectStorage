score = 0 
questions = {
        "What is the capital of France?": "Paris",
        "Who wrote the play 'Romeo and Juliet'?": "Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter",
        "In which year did the Titanic sink?": "1912",
        "What is the name of Batman's City?": "Gotham"
    }

   
for question, correct_answer in questions.items():
       
        user_answer = input(question)

       
        if user_answer.lower() == correct_answer.lower():
            print("Correct! \n")
            score += 1
        else:
            print("Sorry, that's incorrect. The right answer is " + correct_answer + ".\n")

print("Quiz complete! You scored " + str(score) +"/5" 
)
