class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class Quiz():
    def __init__(self):
        self.head = None

    def add_question(self, question):
        if not quiestion: return
        if not self.head: 
            self.head = question
            return 
        

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
        self.players = []

    def get_score(self):
        pass