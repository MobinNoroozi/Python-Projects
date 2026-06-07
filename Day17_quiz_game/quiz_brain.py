""" This is out quiz brain class. Each time we are creating a quiz, there should be certin functionality to placed. """

class QuizBrain:
    
    '''Each quiz object will have 3 attributes. One is the number of questions. One is the list of questions.
        And at the end it is the current score. The quesiton list will be provided from the data file'''
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    '''Lets us to go to the next quesiton in the quiz'''
    def next_question(self):
        current_question = self.question_list[self.question_number]     # Lists start with 0, This hold onto the first question
        self.question_number += 1       # After that we do not need it, we increament the number and for display purpose as well. 
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False): ")       # We show the num of question and the question, and we ask for response
        self.check_answer(user_answer, current_question.answer)      # This function will check the user answer to the correct answer

    # Checks if it user got it right. If yes, increament the score
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That is wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


    # Return true if we still have questions left in our questions list
    def still_has_question(self):
        return (self.question_number < len(self.question_list))
            

