"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。
"""
#菜单
menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

#用 字典嵌套字典 作为数据结构
# students = {}
students ={
    '李思': {'语文成绩': 126.0, '数学成绩': 135.0, '英语成绩': 122.0},
    '张三': {'语文成绩': 96.0, '数学成绩': 135.0, '英语成绩': 88.0},
    '王五': {'语文成绩': 59.0, '数学成绩': 63.0, '英语成绩': 52.0},
    '康康': {'语文成绩': 102.0, '数学成绩': 76.0, '英语成绩': 91.0},
    '小明': {'语文成绩': 88.0, '数学成绩': 95.0, '英语成绩': 75.0},
}

#自定义函数：成绩合法性检验
def score_input(prompt):
    while True:
        try:
            score = float(input(prompt))
        except ValueError:
            print("⚠️ 请输入数字，例如 92 或 92.5")
            continue
        if score < 0 or score >150:
            print(f"⚠️ 「{score}」成绩有误！(0-150)")
            continue
        return score

#自定义函数：读取所有学科成绩
def read_all_scores():
    """依次询问三科成绩，返回一个字典"""
    return {
        "语文成绩": score_input("请输入语文成绩："),
        "数学成绩": score_input("请输入数学成绩："),
        "英语成绩": score_input("请输入英语成绩："),
    }

while True:
    #打印菜单
    print(menu)
    choice = input("请输入要执行的操作(1-7)：").strip()
    match choice:
        case "1":
            # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
            name = input("请输入学生姓名：").strip()
            if not name:
                print("⚠️ 姓名不能为空")
                continue
            if name in students:
                print(f"⚠️ 【{name}】已存在于系统中，请勿重复添加！")
                continue
            student_info = read_all_scores()
            students[name] = student_info
            print(f"添加 【{name}】 成功")

        case "2":
            # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
            name = input("请输入要修改的学生姓名：").strip()
            if not name:
                print("⚠️ 姓名不能为空")
                continue
            if name not in students:
                print(f"⚠️ 【{name}】未存在于系统中，无法进行修改！")
                continue
            student_info = read_all_scores()
            students[name] = student_info
            print(f"修改 【{name}】 成功")

        case "3":
            # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
            name = input("请输入要删除的学生姓名：").strip()
            if not name:
                print("⚠️ 姓名不能为空")
                continue
            if name not in students:
                print(f"⚠️ 【{name}】未存在于系统中，无法进行删除！")
                continue
            del students[name]
            print(f"删除 【{name}】 成功")

        case "4":
            # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
            # students ={'李思': {'语文成绩': '92', '数学成绩': '80', '英语成绩': '78'}}
            name = input("请输入要查询的学生姓名：").strip()
            if not name:
                print("⚠️ 姓名不能为空")
                continue
            if name not in students:
                print(f"⚠️ 【{name}】未存在于系统中，无法进行查询！")
                continue
            for subjects,scores in students[name].items(): #踩坑了!遍历字典只会给key,不给value,要用.items()
                print(f"{subjects} ： {scores}")

        case "5":
            # 5. 列出所有学生：遍历所有学生信息并输出。
            # students ={'李思': {'语文成绩': 92, '数学成绩': 80, '英语成绩': 78}}
            print(f"共有 {len(students)} 名学生")
            print("姓名\t\t\t语文\t\t\t数学\t\t\t英语")
            for name in students.keys():
                print(f"{name}\t\t\t",end = "")
                for scores in students[name].values():
                    print(f"{scores}\t\t",end = "")
                print()

        case "6":
            #6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
            #期望输出：
            # """
            # 语文    最高分：李思 132    最低分：王五 56    平均分：92.8
            # ......
            # """
            #得出 各科成绩列表
            C_score = []
            M_score = []
            E_score = []
            for name in students.keys():
                for i,j in students[name].items():
                    if i == "语文成绩":
                        C_score.append(j)
                    elif i == "数学成绩":
                        M_score.append(j)
                    elif i == "英语成绩":
                        E_score.append(j)
            #得出 各科最高成绩、最低成绩、平均分
            C_max = max(C_score)
            C_min = min(C_score)
            C_average = sum(C_score) / len(C_score)
            M_max = max(M_score)
            M_min = min(M_score)
            M_average = sum(M_score) / len(M_score)
            E_max = max(E_score)
            E_min = min(E_score)
            E_average = sum(E_score) / len(E_score)
            #通过 各科最高成绩、最高成绩 索引出此成绩的 学员姓名
            C_nice_name = []
            C_no_name = []
            M_nice_name = []
            M_no_name = []
            E_nice_name = []
            E_no_name = []
            for name in students.keys():
                for i,j in students[name].items():
                    if i == "语文成绩" and j == C_max:
                        C_nice_name.append(name)
                    elif i == "语文成绩" and j == C_min:
                        C_no_name.append(name)
                    elif i == "数学成绩" and j == M_max:
                        M_nice_name.append(name)
                    elif i == "数学成绩" and j == M_min:
                        M_no_name.append(name)
                    elif i == "英语成绩" and j == E_max:
                        E_nice_name.append(name)
                    elif i == "英语成绩" and j == E_min:
                        E_no_name.append(name)
            #打印结果
            print(f"""
语文\t\t 最高分：{C_nice_name} {C_max}\t\t 最低分：{C_no_name} {C_min}\t\t 平均分：{C_average:.1f}
数学\t\t 最高分：{M_nice_name} {M_max}\t\t 最低分：{M_no_name} {M_min}\t\t 平均分：{M_average:.1f}
英语\t\t 最高分：{E_nice_name} {E_max}\t\t 最低分：{E_no_name} {E_min}\t\t 平均分：{E_average:.1f}
            """)

        case "7":
            # 7. 退出系统。
            print("退出系统，感谢使用！")
            break