import os
file_name = 'Data.txt'

def main():
    while True:
        Menu()
        temp = int(input('请选择：'))
        if temp in [0, 1, 2, 3, 4, 5, 6, 7]:
            if temp == 0:
                answer = input('确定要退出?y/n\n')
                if answer == 'y' or answer == 'Y':
                    print('thanks')
                    break
                else:
                    continue

            elif temp == 1:
                insert()
            elif temp == 2:
                search()
            elif temp == 3:
                delete()
            elif temp == 4:
                modify()
            elif temp == 5:
                sort()
            elif temp == 6:
                totle()
            elif temp == 7:
                show()


def Menu():
    print('========学生信息管理系统===========')
    print('------------功能菜单--------------')
    print('|\t\t\t1、录入学生信息\t\t|')
    print('|\t\t\t2、查找学生信息\t\t|')
    print('|\t\t\t3、删除学生信息\t\t|')
    print('|\t\t\t4、修改学生信息\t\t|')
    print('|\t\t\t5、排序\t\t\t\t|')
    print('|\t\t\t6、统计学生总人数\t\t|')
    print('|\t\t\t7、显示所有学生信息\t\t|')
    print('|\t\t\t0、退出系统\t\t\t|')
    print('---------------------------------')


def insert():
    student_list = []
    while True:
        id = input('请输入id（如1001）')
        if not id:
            break
        name = input('请输入姓名')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入java成绩'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        temp = input('是否继续添加？y/n')
        if temp == 'y':
            continue
        else:
            break
    save(student_list)
    print('保存完成')

def save(lst):
    try:
        stu_data = open(file_name, 'a', encoding='utf-8')
    except:
        stu_data = open(file_name, 'w', encoding='utf-8')
    for ele in lst:
        stu_data.write(str(ele)+'\n')
    stu_data.close()

def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(file_name):
            ans = input('按id查找输入1，按姓名查找输入2')
            if ans == '1':
                id = input('请输入学生id')
            elif ans == '2':
                name = input('请输入学生姓名')
            else:
                print('输入有误，请重新输入')
                search()
            with open(file_name, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            ans = input('是否要继续查询？y/n')
            if ans == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return

def show_student(lst):
    if len(lst) == 0:
        print('未查询到学生信息，无数据显示！')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'), item.get('name'),
                                 item.get('english'), item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))


def delete():
    while True:
        student_id = input('请输入要删除的学生id:')
        if student_id != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(file_name, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for ele in student_old:
                        d = dict(eval(ele))
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id 为{student_id}的学生信息已被删除')
                    else:
                        print(f'没找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()
            answer = input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入你要修改的学生ID:')
    with open(file_name, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到了，可以修改：')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = input('请输入英语成绩')
                        d['python'] = input('请输入python成绩')
                        d['java'] = input('请输入Java成绩')
                    except:
                        print('输入信息有误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
            ans = input('是否继续修改其他学生信息？y/n')
            if ans == 'y':
                modify()
            else:
                pass




def sort():
    if os.path.exists(file_name):
        with open(file_name,'r',encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        print('文件不存在')
    ans1 = input('请选择\n1、升序\n2、降序\n')
    if ans1 == '1':
        judge = False
    elif ans1 == '2':
        judge = True
    else:
        print('请重新输入')
        sort()
    ans2 = input('请选择排序方式：\n1、按英语排序\n2、按python成绩排序\n3、按Java成绩排序\n4、按总成绩排序\n')
    if ans2 == '1':
        student_new.sort(key=lambda student_new :int(student_new['english']), reverse= judge)
    elif ans2 == '2':
        student_new.sort(key=lambda student_new: int(student_new['python']), reverse=judge)
    elif ans2 == '3':
        student_new.sort(key=lambda student_new: int(student_new['java']), reverse=judge)
    elif ans2 == '4':
        student_new.sort(key=lambda student_new: int(student_new['english'])+int(student_new['java'])+int(student_new['python']), reverse=judge)
    else:
        print('输入有误，重新输入')
        sort()
    show_student(student_new)
    
    
def totle():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据')


def show():
    student_list = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_list.append(eval(item))
        show_student(student_list)
    else:
        print("文件不存在")


main()

