from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] # List that will hold our Question objects with correct attributes

for question in question_data: # This is the dictionaries
    question_text = question["text"] # We hold onto the text and answer
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer) # For each quesiton in data, we create a qustion object and assigns it with text and correct answer
    question_bank.append(new_question) # Then we add it to the list


quiz = QuizBrain(question_bank) # We initialize our quiz object that will handle the quiz logic


# Quiz has a function that checks if there are questions left
while quiz.still_has_question():
    quiz.next_question() #Go to the next question. The quiz brain will check for the answers and verifies

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
