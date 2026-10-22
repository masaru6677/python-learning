# 任务 1 · 求和函数（*args）
# 要求做到：
# print(sum_all(1, 2, 3))           # 6
# print(sum_all(10))                # 10
# print(sum_all(1, 2, 3, 4, 5))     # 15
# print(sum_all())                  # 0    ← 一个都没传，要返回 0，不能报错

def sum_all(*nums):
    """
    计算所有传入数字的和
    :param nums: 需要求和的这批数据
    :return: 所有传入数字的和
    """
    return sum(nums)
print(sum_all(1, 2, 3))           # 6
print(sum_all(10))                      # 10
print(sum_all(1, 2, 3, 4, 5))     # 15
print(sum_all())                      # 0    ← 一个都没传，要返回 0，不能报错

# 任务 2 · 学生信息格式化
# 要求做到：
# show_student(姓名="张三", 语文=96, 数学=135)
# # 张三 | 语文=96 | 数学=135
#
# show_student(姓名="李四", 英语=88)
# # 李四 | 英语=88
#
# show_student()
# # （什么都没传，输出一个空行或者提示，不要报错）

def show_student(**info):
    if not info:
        print("空输入！")
        return
    parts = [f"{k}={v}" for k, v in info.items()]
    print(" | ".join(parts))
show_student(姓名="张三", 语文=96, 数学=135)
show_student(姓名="李四", 英语=88)
show_student()

# 任务 3 · 两个都要
# 要求做到：
# log("开始处理", 100, 200, 用户="张三", 状态="成功")
# 输出：
# 位置参数 (3 个): ('开始处理', 100, 200)
# 关键字参数 (2 个): {'用户': '张三', '状态': '成功'}
def log(*args, **kwargs):
    """同时接收任意位置参数和任意关键字参数，分别打印"""
    print(f"位置参数 ({len(args)} 个): {args}")
    print(f"关键字参数 ({len(kwargs)} 个): {kwargs}")
log("开始处理", 100, 200, 用户="张三", 状态="成功")

# 任务 4 · 为什么需要它
# 任务：自己写一个"简易版 print"，支持任意多个参数 + sep 关键字：
def my_print(*args, sep=" "):
    """把参数用 sep 连接后打印一行"""
    print(sep.join(str(x) for x in args))
my_print("a", "b", "c")           # a b c
my_print("a", "b", "c", sep="-")  # a-b-c
my_print("x")                     # x
my_print(1233423)