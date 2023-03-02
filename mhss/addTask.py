import os


class addTask:
    def __init__(self):
        pass

    def show(self, conn, controller):
        # os.system('cls')
        os.system('clear')

        title = input("Thêm một nhiệm vụ: ")
        time = input("Thêm hạn chót: ")
        p = int(input("Thêm thứ tự ưu tiên:"))

        conn.add(title, time, p)
        controller.setScreen(0)