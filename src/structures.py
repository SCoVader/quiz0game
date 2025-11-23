class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

class Quiz:
    def add_to_head(self, node):
        node.next = self.head
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
        

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