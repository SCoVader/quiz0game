
def demo():
    import logging
    import threading
    from quiz0_server import Quiz0Server
    from quiz0_handler import Quiz0RequestHandler
    logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s')

    address = ('localhost', 0) # let the kernel give us a port
    server = Quiz0Server(address, Quiz0RequestHandler)
    ip, port = server.server_address # find out what port we were given

    t = threading.Thread(target=server.serve_forever)
    # t.setDaemon(True) # don't hang on exit
    t.daemon = True # don't hang on exit
    t.start()

    logger = logging.getLogger('client')
    logger.info('Server on %s:%s', ip, port)

    # Connect to the server
    logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connecting to server')
    s.connect((ip, port))

    # Send the data
    message = 'Hello, world'
    logger.debug('sending data: "%s"', message)
    # len_sent = s.send(message)
    len_sent = s.send(bytes(message, 'utf-8'))

    # Receive a response
    logger.debug('waiting for response')
    response = s.recv(len_sent)
    logger.debug('response from server: "%s"', response)

    # Clean up
    logger.debug('closing socket')
    s.close()
    logger.debug('done')
    server.socket.close()

def db_demo():

    import os
    import sqlite3

    db_path = "tutorial.db"
    if os.path.exists(db_path):
        os.remove(db_path)


    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    q = cursor.execute("create table movie(title, year, score)")
    print(q.fetchone())
    cursor.execute("""INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """)
    connection.commit()

    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0)
    ]
    cursor.executemany("insert into movie values(?, ?, ?)", data)
    connection.commit()

    for row in cursor.execute("SELECT year, title FROM movie ORDER BY year"):
        print(row)

    connection.close()

    new_con = sqlite3.connect("tutorial.db")
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
    title, year = res.fetchone()
    print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
    new_con.close()

def dbconn_demo():
    from db import DBConnector

    dbcon = DBConnector("quiz0.db")

    test_player = {"name": "test_add_player", "color": 3}
    dbcon.add_player(test_player, "qwerty20")

    test_quiz0 = {
            "name": "Title of my test Quiz0!",
            "author": test_player,
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
    dbcon.add_quiz0(test_quiz0)
    dbcon.close()

if __name__ == '__main__':
    # Register/Login
    # Create Quiz
    
    # Select quiz by number
    # get question
    # give ansver
    # next
    pass