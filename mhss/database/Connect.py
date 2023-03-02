import json

import psycopg2 as psycopg2


class Connect:
    def __init__(self):
        f = open("database/configure.json")
        db = json.load(f)
        self.conn = psycopg2.connect(**db)

        self.cur = self.conn.cursor()

    def createTable(self):
        createScrip = "CREATE TABLE IF NOT EXISTS todoList (Id SERIAL, Title VARCHAR(255) NOT NULL, Time VARCHAR(255), Priority INT)"
        self.cur.execute(createScrip)
        self.conn.commit()

    def getAll(self):
        self.cur.execute('SELECT * FROM todoList ORDER BY id ASC')
        self.conn.commit()
        return self.cur.fetchall()
    
    def updateTable(self, id_selected, title, time, priority):
        self.cur.execute(f"UPDATE public.todoList SET title='{title}', time = '{time}', priority = '{priority}' where id={id_selected}")
        self.conn.commit()

    def add(self, title, time, priority):
        addScript = "INSERT INTO todoList (title, time, priority) VALUES (%s, %s, %s)";
        Record = (title, time, priority)
        self.cur.execute(addScript, Record)
        self.conn.commit()
    def delete(self, id_selected):
        self.cur.execute(f"DELETE FROM todoList WHERE Id = {id_selected}")
