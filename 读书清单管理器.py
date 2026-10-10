# ========= 我的读书清单 =========
# 1. 增
# 2. 删
# 3. 改
# 4. 查
# 5. 统计
# 0. 退出
# ================================

#菜单
menu = """
========= 我的读书清单 =========
1. 增
2. 删
3. 改
4. 查
5. 统计
6. 退出
================================
"""
#清单 根据视频 清单本体是字典 内部嵌套字典作为详情
#ai要求外层列表 内部嵌套字典    *****但是先按视频来
books = {
        "人类简史":{"books_author":"尤瓦尔·赫拉利","books_status":"在读"},
        "活着":{"books_author":"余华","books_status":"读完"}
                                                                     }
# books = {}

#拦空输入
def ask_not_empty(prompt):
    """反复询问，直到用户输入非空内容，返回结果"""
    while True:
        value = input(prompt).strip()      # ← strip 去掉两端空格
        if value:
            return value
        print("⚠️ 输入不能为空，请重新输入")

#未知循环次数 while循环
while True:
    print(menu)
    #match模式匹配 避免繁琐if语句
    choice = input("请输入要执行的操作(1-6)：").strip()
    match choice:
        # 增
        case "1":
            # 字典嵌套字典 从外层看 书名为keys
            books_title = ask_not_empty("请输入书名：")
            if books_title in books:
                print("此书已存在于清单中，请重新选择操作!")
                continue
            # 字典嵌套字典 作者、状态为外层字典的value值
            books_author = ask_not_empty("请输入作者：")
            while True:
                books_status = input("请输入状态(想读/在读/读完)：")
                if books_status in ("想读","在读","读完"):
                    break
                print(f"⚠️ 「{books_status}」不是有效状态")
            books[books_title] = {"books_author":books_author,"books_status":books_status}#增
        #删
        case "2":
            while True:
                books_title = input("请输入要删除的书名：")
                if books_title in books:
                    break
                print(f"⚠️ 「{books_title}」不是有效书名")
            del books[books_title]
            print("删除成功")
        #改
        case "3":
            while True:
                books_title = input("请输入要更改的书名：")
                if books_title in books:
                    break
                print(f"⚠️ 「{books_title}」不是有效书名")
            while True:
                confirm_author = input("是否需要更改作者(是/否)：")
                if confirm_author not in ("是","否"):
                    print("请求错误!请重新选择：")
                    continue
                elif confirm_author == "是":
                    books_author = input("要将原作者更改成：")
                    # for m in books.keys():
                    #     if m == books_title:
                    #         books_info = books[books_title]
                    #         books_info["books_author"] = books_author
                    #繁琐改良
                    books[books_title]["books_author"] = books_author
                    break
                elif confirm_author == "否":
                    break
            while True:
                confirm_status = input("是否需要更改状态(是/否)：")
                if confirm_status not in ("是","否"):
                    print("请求错误!请重新选择：")
                    continue
                elif confirm_status == "是":
                    while True:
                        books_status = input("要将原状态更改成(想读/在读/读完)：")
                        if books_status in ("想读","在读","读完"):
                            # for n in books.keys():
                            #     if n == books_title:
                            #         books_info = books[books_title]
                            #         books_info["books_status"] = books_status
                            # 繁琐改良
                            books[books_title]["books_status"] = books_status
                            break
                        print(f"⚠️ 「{books_status}」不是有效状态")
                    break
                elif confirm_status == "否":
                    break
            print("更改成功")
        #查
        #"""
        # ---------- 共 2 本书 ----------
        # 1. 《人类简史》 / 尤瓦尔·赫拉利 / [在读]
        # 2. 《活着》 / 余华 / [读完]
        # ------------------------------
        #"""
        case "4":
            print(f"---------- 共 {len(books)} 本书 ----------")
            n = 1
            for books_title in books.keys():
                books_info = books[books_title]
                print(f"{n}. 《{books_title}》 / {books_info["books_author"]} / [{books_info["books_status"]}]")
                n += 1
            print("------------------------------")

        #统计
        #"""
        #---------- 统计 ----------
        # 总计：5 本
        # 想读：2 本
        # 在读：1 本
        # 读完：2 本
        #--------------------------
        #"""
        case "5":
            #for循环遍历books_status，统计各个状态的书本个数
            x,y,z = 0,0,0
            for title in books:
                books_info = books[title]
                i = books_info["books_status"]
                if i == "想读":
                    x += 1
                elif i == "在读":
                    y += 1
                elif i == "读完":
                    z += 1
            print(f"""
---------- 统计 ----------
总计：{len(books)} 本
想读：{x} 本
在读：{y} 本
读完：{z} 本
--------------------------
            """)
        #退出
        case "6":
            print("退出程序，感谢使用!")
            break
        #错误操作
        case _:
            print("操作错误!请重新选择操作(1-6)!")








