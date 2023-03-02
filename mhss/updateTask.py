from database.Connect import Connect

def updateTask():
    connect = Connect()
    table = connect.getAll()

    id_list = []
    for i in table: 
        id_list.append(i[0])

    id = int(input("id của task muốn sửa: "))
    if id in id_list:
        title = input("Sửa tiêu đề thành: ")
        time = input("Sửa thời gian thành: ")
        priority = input("Sửa độ ưu tiên thành: ")
        connect.updateTable(id, title, time, priority)

        print("Sửa thành công")

    else:
        print("Id không tồn tại, vui lòng thử lại sau")


