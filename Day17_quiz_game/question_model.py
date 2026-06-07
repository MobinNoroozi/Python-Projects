"""This is the question class that shapes each qustion.
    We do not want it in terms of dictionaries because that will be too complicated.
    We turn them into object which is easier to work with.
    Here each qustion object has a text and an answer which will be assignesd to them when they are initialized."""

class Question:
    
    # text and answer are attributes and will be initialized using q_text and q_answer
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer



