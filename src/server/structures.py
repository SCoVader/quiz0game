class Question():
    def __init__(self, text, answers, right, timer = 0):
        self.text = text # Question text that will be displayed to players
        self.answers = answers # list if strings representing possible answers
        self.right = right # List of indexes of correct answers. Can't be empty, can't contain all answers
        self.timer = timer # Time ofter which question will be skipped in seconds. 0 - unlimited time, default option

class Room():
    def __init__(self, id, creator, questions):
        self.id = id
        self.creator = creator
        self.questions = questions
        self.players=[]