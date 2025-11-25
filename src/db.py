import sqlite3

class DBConnector():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def add_player(self, player, password):
        passwd = hash(password)
        self.cursor.execute("INSERT INTO players(name, pass, color) VALUES (?, ?, ?)", (player['name'], passwd, player['color']))
        self.connection.commit()
        return

    '''
    quiz0 = 
        {
            "name": "Title of your Quiz0!",
            "author": {
                "name": "player_name",
                "color": "player_color"
            },
            "questions": [
                {
                    "text": "First questions to players",
                    "answers": ["answer_one", "answer_two", "correct_answer", "answer_four"],
                    "correct": 2
                },
                {
                    "text": "Second questions to players",
                    "answers": ["correct_answer", "answer_two", "answer_three", "answer_four"],
                    "correct": 0
                },

            ]
        }
    '''
    def get_player_id(self, player):
        result = self.cursor.execute("SELECT id FROM players WHERE name IS ? AND ?", (player["name"], player["color"]))
        return result.fetchone()

    def get_quiz0_id(self, quiz0_name):
        print(quiz0_name)
        result = self.cursor.execute("SELECT id FROM players WHERE name IS (?)", (quiz0_name,))
        return result.fetchone()

    def get_question_id(self, question_text):
        result = self.cursor.execute("SELECT id FROM players WHERE name IS (?)", (question_text,))
        return result.fetchone()

    def add_quiz0(self, quiz0):
        author_id = self.get_player_id(quiz0["author"])
        
        self.cursor.execute("INSERT INTO quiz0s(name, author) VALUES (?, ?)", (quiz0["name"], author_id[0]))
        self.connection.commit()
        quiz0_id = self.get_quiz0_id(quiz0["name"])
        for question in quiz0["questions"]:
            self.cursor.execute("INSERT INTO question(quiz0_id, text) VALUES(?, ?)", (quiz0_id, question["text"]))
            self.connection.commit()
            question_id = self.get_question_id(question["text"])
            for idx, answer in enumerate(question["answers"]):
                self.cursor.execute("INSERT INTO answer(question_id, text, is_correct) VALUES(?, ?, ?)", (question_id, answer, 1 if idx == question["correct"] else 0))
                self.connection.commit()

            

        # CREATE TABLE `question` (`id*`, `quiz0_id`, `text`)
        # CREATE TABLE `answer` (`id*`, `question_id`, `text`, `is_correct`)