from tabulate import tabulate
from database.Connect import Connect
import updateTask
import os
from addTask import addTask
from deleteTask import deleteTask
class Screen:
    def __init__(self):
        self.screen = 0

    def setScreen(self, id):
        self.screen = id


def select_func(controller):
    # Chức năng
    print("\nCHỨC NĂNG")
    print("1. Thêm todo")
    print("2. Sửa todo")
    print("3. Xoá todo")
    print("4. Sắp xếp theo")
    print("5. Thoát")

    while True:
        func_selected = int(input("\nMời bạn chọn chức năng: "))
        # Thêm
        if func_selected == 1:
            controller.setScreen(1)
            break
        # Sửa
        elif func_selected == 2:
            updateTask.updateTask()
            # os.system('cls')
            os.system('clear')
            # Main_screen()
            controller.setScreen(0)
            break
        # Xoá
        elif func_selected == 3:
            controller.setScreen(3)
            break
        # Sắp xếp
        elif func_selected == 4:
            pass
        elif func_selected == 5:
            controller.setScreen(5)
            break
        else:
            print("\nChọn sai chức năng! \nVui lòng lựa chọn lại.\n")
            continue


def Main_screen(connect, controller):
    todos = connect.getAll()
    # Main Screen
    print("=" * 35 + "  " + "TODO APP" + "  " + "=" * 34)
    print("=" * 81)
    print(tabulate(todos, headers=['Id', 'Todo', 'Thời gian', 'Ưu tiên'], tablefmt='orgtbl'))
    print("=" * 81)

    select_func(controller)


if __name__ == '__main__':
    connect = Connect()
    connect.createTable()
    controller = Screen()
    addScreen = addTask()
    deleteScreen = deleteTask()

    running = True
    while running:
        os.system('clear')
        # os.system('cls')
        if controller.screen == 0:
            Main_screen(connect, controller)
        elif controller.screen == 1:
            addScreen.show(connect, controller)
        elif controller.screen == 3:
            deleteScreen.show(connect, controller)
        elif controller.screen == 5:
            running = False
        else:
            pass


