import os
from tabulate import tabulate
from database.Connect import Connect
import psycopg2 as psycopg2

class deleteTask:
    def __int__(self):
        pass

    def show(self, connect, controller):
        todos = connect.getAll()

        print(tabulate(todos, headers=['Id', 'Todo', 'Thời gian', 'Ưu tiên'], tablefmt='orgtbl'))

        p = input("Chon id ma ban muon xoa: ")
        connect.delete(p)
        controller.setScreen(0)
