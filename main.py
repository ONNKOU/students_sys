from func import list_load, person_add, list_show, person_del

def main_func():
    students_list = list_load()
    while True:
        print("======欢迎使用学生信息系统======")
        print("1添加\n2查看列表\n3删除\n4退出\n")
        choice = input("请选择:")
        if choice == "1":
            students_list = person_add(students_list)
        elif choice == "2":
            list_show(students_list)
        elif choice == "3":
            students_list = person_del(students_list)
        elif choice == "4":
            break
        else:
            print("未知指令")


if __name__ == "__main__":
    main_func()