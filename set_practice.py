# 练去重、交并差

#第 1 题 · 邮件列表去重
#场景：你从两个表格里导出了收件人，合并后有很多重复。发重复的邮件会被人投诉。
emails = [
    "li@qq.com", "zhang@163.com", "li@qq.com",
    "wang@gmail.com", "zhang@163.com", "li@qq.com",
]
#要求输出
# 去重前：6 个
# 去重后：3 个
# 收件人：li@qq.com zhang@163.com wang@gmail.com
emails_1 = {*emails} #set(emails)
print(f"去重前：{len(emails)} 个")
print(f"去重后：{len(emails_1)} 个")
# print(f"收件人：{emails_1}")
print(f"收件人：{' '.join(emails_1)}")

# 第 2 题 · 找共同好友
# 场景：给两个人推荐"可能认识的人"。
alice = {"张三", "李四", "王五", "赵六"}
bob = {"李四", "王五", "孙七"}
# 要求输出：
# 共同好友：{'李四', '王五'}
# 所有好友：...（两人合起来一共认识谁）
# 只有 Alice 认识：...（Bob 不认识的那些）
# 只有 Bob 认识：...
# 两人总共认识几个人：5

# 用方法名
print(f"共同好友：{alice.intersection(bob)}")
print(f"所有好友：{alice.union(bob)}")
print(f"只有 Alice 认识：{alice.difference(bob)}")
print(f"只有 Bob 认识：{bob.difference(alice)}")
print(f"两人总共认识几个人：{len(alice.union(bob))}")
# 用符号
print(f"共同好友：{alice & bob}")
print(f"所有好友：{alice | bob}")
print(f"只有 Alice 认识：{alice - bob}")
print(f"只有 Bob 认识：{bob - alice}")
print(f"两人总共认识几个人：{len(alice | bob)}")

#第 3 题 · 用户标签分析
# 场景：这是真实业务里天天在干的事——给用户打标签，然后算相似度。
user_a = {"Python", "算法", "篮球", "科幻", "考研"}
user_b = {"Python", "算法", "吉他", "科幻", "旅行"}
# 要求输出：
# 共同兴趣：{'Python', '算法', '科幻'}
# 共同兴趣数量：3
# 两人兴趣总覆盖：7 个
# A 有 B 没有的兴趣：{'篮球', '考研'}
# 给 A 推荐（B 有但 A 没有）：{'吉他', '旅行'}
# "吉他" 是 A 的兴趣吗？False
print(f"共同兴趣：{user_a & user_b}")
print(f"共同兴趣数量：{len(user_a & user_b)}")
print(f"两人兴趣总覆盖：{len(user_a | user_b)}")
print(f"A 有 B 没有的兴趣：{user_a - user_b}")
print(f"给 A 推荐（B 有但 A 没有）：{user_b - user_a}")
# if "吉他" in user_a:
#     x = True
# else:
#     x = False
# print(f"\"吉他\" 是 A 的兴趣吗？{x}")
# in 本身返回的就是 True / False，直接打印就行：
print(f"\"吉他\" 是 A 的兴趣吗？{'吉他' in user_a}")
#我认为的"兴趣相似度"公式为 len(user_a & user_b) / len(user_a | user_b)
print(f"\"兴趣相似度\"为{len(user_a & user_b) / len(user_a | user_b)}")

# 第 4 题 · 去重但保持顺序
# 场景：你在做"统计一段英文里出现过哪些单词"。集合能去重，但集合没有顺序——输出会乱成一团。可你想要的是"按首次出现的顺序列出所有不重复的词"。
words = ["apple", "banana", "apple", "cherry", "banana", "date", "apple"]
#要求输出
# 不同单词共 4 个
# 依次是：apple banana cherry date
words_list = list()
for i in words:
    if i not in words_list:
        words_list.append(i)
print(f"不同单词共 {len(words_list)} 个")
print(f"依次是：{words_list}")

# #第4题 答案
# #in 用在列表上 = 挨个找；in 用在集合/字典上 = 一步到位。
# seen = set()        # ← 集合负责"见过没有"，O(1)
# result = []         # ← 列表负责"记住顺序"
#
# for w in words:
#     if w not in seen:      # 集合判断，瞬间完成
#         seen.add(w)
#         result.append(w)

# 第 5 题 · 挑战题
#场景：给你两段文本，找出只有第一段出现过、第二段没出现过的词。
text1 = "python is a good language and python is easy"
text2 = "java is also a good language"
#要求输出：
# text1 独有的词：{'python', 'and', 'easy'}
x = {*(text1.split())} - {*(text2.split())}
print(f"text1 独有的词：{x}")