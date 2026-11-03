import os
# 第 1 步 · 只列当前目录（不递归）
# def list_py_files(path):
#     """列出 path 目录下的 .py 文件（不看子文件夹）"""
#     for i in os.listdir(path):
#         # if i[-3:] == ".py":
#         if os.path.isfile(i) and i.endswith(".py"):
#             print(i)
# list_py_files(".")

# 第 2 步 · 递归（核心）
# 任务：遇到文件夹就钻进去继续找
# def find_py_files(path):
#     """递归找出 path 及其所有子目录下的 .py 文件，返回列表"""
#     result = []
#     # 1.如果path是文件 → 判断是不是.py，是就返回[它]
#     if os.path.isfile(path):
#         if path.endswith(".py"):
#             result.append(path)
#     # 2.如果path是文件夹 → 遍历里面每一样东西，对每一样递归调用自己
#     else:
#         for i in os.listdir(path):
#             result += find_py_files(os.path.join(path, i))
#     # 3.把所有人的结果拼起来返回
#     return result
# print(find_py_files("."))

# 第 3 步 · 排除指定目录（实战必需）
# def find_py_files(path, skip=(".venv", ".git", "__pycache__")):
#     """递归找出 path 及其所有子目录下的 .py 文件，返回列表"""
#     result = []
#     # 1.如果path是文件 → 判断是不是.py，是就返回[它]
#     if os.path.isfile(path):
#         if path.endswith(".py"):
#             result.append(path)
#     # 2.如果path是文件夹 → 遍历里面每一样东西，对每一样递归调用自己
#     else:
#         for i in os.listdir(path):
#             if i in skip:  # ← 用 in 判断，元组，不是字符串
#                 continue
#             result += find_py_files(os.path.join(path, i), skip)
#     # 3.把所有人的结果拼起来返回
#     return result
# print(find_py_files("."))

# # 第 4 步 · 完整版（加统计）
# def find_py_files(path, skip=(".venv", ".git", "__pycache__")):
#     """递归找出 path 及其所有子目录下的 .py 文件，返回列表"""
#     result = []
#     # 1.如果path是文件 → 判断是不是.py，是就返回[它]
#     if os.path.isfile(path):
#         if path.endswith(".py"):
#             result.append(path)
#     # 2.如果path是文件夹 → 遍历里面每一样东西，对每一样递归调用自己
#     else:
#         for i in os.listdir(path):
#             if i in skip:  # ← 用 in 判断，元组，不是字符串
#                 continue
#             result += find_py_files(os.path.join(path, i), skip)
#     # # 3.把所有人的结果拼起来返回
#     # return result
#
#     # 只显示文件名，不显示完整路径
#     result_1 = []
#     for j in result:
#         result_1.append(os.path.basename(j))
#     # 按文件名排序
#     result_1.sort()
#
#     return result_1
#
# result_print = find_py_files(".")
# # 统计文件个数
# print(f"共找到 {len(result_print)} 个 .py 文件：")
# # 显示文件大小
# for name in result_print:
#     size = os.path.getsize(name)
#     print(f"{name:<40} {size:>8} 字节")

# 第 4 步    修改
def find_py_files(path, skip=(".venv", ".git", "__pycache__")):
    """递归找出所有 .py 文件的完整路径"""
    result = []
    if os.path.isfile(path):
        if path.endswith(".py"):
            result.append(path)          # ← 存完整路径
    else:
        for i in os.listdir(path):
            if i in skip:
                continue
            result += find_py_files(os.path.join(path, i), skip)
    return result
paths = find_py_files(".")
paths.sort()                                  # 按完整路径排序

print(f"共找到 {len(paths)} 个 .py 文件：\n")
for p in paths:
    name = os.path.basename(p)                # 显示时才取名字
    size = os.path.getsize(p)                 # 用完整路径取大小 ✅
    print(f"{name:<40} {size:>8} 字节")