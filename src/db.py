import sqlite3
from urllib.request import pathname2url

class DBConnector():

    def create_db(self, db):
        conn = sqlite3.connect(db)
        curs = conn.cursor()
        curs.execute('CREATE TABLE "players" (`id` INTEGER PRIMARY KEY UNIQUE NOT NULL, `name` TEXT, `pass` TEXT, `color` INTEGER)')
        curs.execute('CREATE TABLE "quiz0s" (`id` INTEGER PRIMARY KEY UNIQUE NOT NULL, `name` TEXT, `author` INTEGER REFERENCES `players`(`id`))')
        curs.execute('CREATE TABLE "questions" (`id` INTEGER PRIMARY KEY UNIQUE NOT NULL, `quiz0_id` INTEGER REFERENCES `quiz0s`(`id`), `text` TEXT NOT NULL)')
        curs.execute('CREATE TABLE "answers" (`id` INTEGER PRIMARY KEY UNIQUE NOT NULL, `question_id` INTEGER REFERENCES `questions`(`id`), `text` TEXT NOT NULL, `is_correct` INTEGER)')
        return (conn, curs)


    def __init__(self, db):
        try:
            dburi = 'file:{}?mode=rw'.format(pathname2url(db))
            self.connection = sqlite3.connect(dburi, uri=True)
            self.cursor = self.connection.cursor()
        except sqlite3.OperationalError:
            conncurs = self.create_db(db)
            self.connection = conncurs[0]
            self.cursor = conncurs[1]

    def close(self):
        self.connection.close()

    def add_player(self, player, password):
        passwd = hash(password)
        self.cursor.execute("INSERT INTO players(name, pass, color) VALUES (?, ?, ?)", (player['name'], passwd, player['color']))
        self.connection.commit()
        return self.cursor.lastrowid

    def add_question(self, quiz0_id, text):
        self.cursor.execute("INSERT INTO questions(quiz0_id, text) VALUES(?, ?)", (quiz0_id, text))
        self.connection.commit()
        return self.cursor.lastrowid

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
        quiz0_id = self.cursor.lastrowid
        for question in quiz0["questions"]:
            question_id = self.add_question(quiz0_id, question["text"])
            for idx, answer in enumerate(question["answers"]):
                self.cursor.execute("INSERT INTO answer(question_id, text, is_correct) VALUES(?, ?, ?)", (question_id, answer, 1 if idx == question["correct"] else 0))
                self.connection.commit()
