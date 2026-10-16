import json


def list_load(): #加载学生信息到列表
    students_list = []
    try:
        with open("students_list_f.json", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    stu = json.loads(line)
                    students_list.append(stu)
    except FileNotFoundError:
        print("未找到记录，已新建列表")
    return students_list


def person_add(students_list): #添加学生信息函数
    person = {}
    try:
        person_name = input("请输入姓名：")
        person_score = int(input("请输入分数："))
        person_age = int(input("请输入年龄："))
    
        person = {"name": person_name, "score": person_score, "age": person_age}
        print(person)
        students_list.append(person)

        with open("students_list_f.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(person, ensure_ascii=False)+"\n")
        print("写入成功")
        
    except ValueError:
        print("输入错误")
    return students_list

def list_show(students_list): #展示学生信息函数
    if not students_list:
        print("无学生信息")
        return
    print("\n===学生信息列表===")
    for idx, item in enumerate(students_list, start=1):
        print(f"{idx}.姓名:{item['name']},分数:{item['score']},年龄:{item['age']}")

def person_del(students_list):
    if not students_list:
        print("列表无信息")
        return students_list
   
    list_show(students_list)

    has_del = False
    while True:  
        try:    
            choice = int(input("请选择要删除的序号：\n按0可返回"))
        except ValueError:
            print("请输入有效序号")
            continue

        choice_num = choice - 1
        if choice_num == -1:
            break
        elif choice_num >= 0 and choice_num < len(students_list):
            del students_list[choice_num]
            list_show(students_list)
            has_del = True
        else:
            print("请输入有效序号")
        

    if has_del == True:
        with open("students_list_f.json", "w", encoding="utf-8") as f:
            for stu in students_list:
                f.write(json.dumps(stu, ensure_ascii=False)+"\n")    
            print("删除成功")
            return students_list
    else:
        return students_list
