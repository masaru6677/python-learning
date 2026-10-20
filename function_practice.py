# 第 1 题 · 没有参数，也没有返回值
def say_hello():
    """打印一句问候"""
    print("""
==========
欢迎使用成绩管理系统
==========
    """)
say_hello()
x = say_hello()
print(f"{x}") #没有 return 的函数，调用结果是  None

# 第 2 题 · 有参数，但没有返回值
def make_line(title, width=30):
    """打印一条以 title 居中的分隔线"""
    # for i in range(width):
    #     if i == width / 2:
    #         print(f" {title} ",end = "")
    #     print("-",end = "")
    #     if i == width - 1:
    #         print()
    print(title.center(width, "-"))
make_line("语文")
make_line("很长的标题", 50)

# 第 3 题 · 有参数，也有返回值
def average(scores):
    """算一组成绩的平均分，返回结果"""
    return round(sum(scores) / len(scores),1)
print(average([90, 80, 70]))        # 80.0
print(average([100, 95]))           # 97.5
result = average([60, 70, 80])
print(result * 2)                    # 140.0