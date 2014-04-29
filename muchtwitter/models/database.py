import sqlite3


class Database():
    HAPPY_WORDS = 'happywords'
    SAD_WORDS = 'sadwords'
    PROFANE_WORDS = 'profane'
    ANGRY_WORDS = 'angrywords'

    query = 'SELECT * FROM %s'

    def __init__(self):
        self.conn = sqlite3.connect('data')
        self.c = self.conn.cursor()

    def get_happywords(self):
        words = [row[0] for row in self.c.execute(Database.query % Database.HAPPY_WORDS)]
        return words

    def get_sadwords(self):
        words = [row[0] for row in self.c.execute(Database.query % Database.SAD_WORDS)]
        return words

    def get_profanewords(self):
        words = [row[0] for row in self.c.execute(Database.query % Database.PROFANE_WORDS)]
        return words

    def get_angrywords(self):
        words = [row[0] for row in self.c.execute(Database.query % Database.ANGRY_WORDS)]
        return words