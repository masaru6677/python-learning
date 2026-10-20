text = """The quick brown fox jumps over the lazy dog.
The dog barks and the fox runs away.
A quick fox is a smart fox, and a smart fox is a quick fox."""

# 任务 1 · 清洗文本
import re
#三个函数封装成一个函数：
def clean_words(s):
    """把一段文本清洗成干净的单词列表"""
    s = s.lower()
    # \s 表示"任意空白"（空格、换行、制表符）;加 r 前缀是为了正则里的 \s 不被当成普通转义
    words = re.split(r"[,.\s]", s)          # 一次切开
    words = [w for w in words if w]        # 去掉空串
    return words

clean_text = clean_words(text)

# 任务 2 · 用集合去重
# 要求输出：
# 总词数：32
# 不同单词数：15
# 不重复的词：{'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'barks', 'and', 'runs', 'away', 'a', 'is', 'smart'}   ← 顺序无所谓
seen = set()        # ← 集合负责"见过没有"，O(1)
result = []         # ← 列表负责"记住顺序"
for w in clean_text:
    if w not in seen:
        seen.add(w)
        result.append(w)
print(f"总词数：{len(clean_text)}")
print(f"不同单词数：{len(seen)}")
print(f"不重复的词：{seen}")

# 任务 3 · 词频统计
# 要求输出（按出现次数从高到低）：
# the    ：4 次
# fox    ：4 次
# a      ：3 次
# is     ：3 次
# quick  ：3 次
# ...
# dog    ：2 次
# ...
# brown  ：1 次

#创建字典用于统计词频
word_counts = {}
for a in clean_text:
    word_counts[a] = word_counts.get(a, 0) + 1     # 一行搞定，不用预置 0
#先把计数做对，排序留到学完 lambda 再说
#遍历word_counts 规范输出
for o,p in word_counts.items():
    print(f"{o} : {p} 次")

# 任务 4 · 集合运算
# 要求：把 text 拆成三句话（按 . 切），然后：
# 第一句独有的词（没在第二、三句出现）：
# 三句都出现的词：

text_123 = text.split(".")

#处理 text_1、text_2、text_3 ————> 干净单词列表 ————> 集合   set() 直接吃一个列表
s1 = set(clean_words(text_123[0]))
s2 = set(clean_words(text_123[1]))
s3 = set(clean_words(text_123[2]))

# 第一句独有的词（没在第二、三句出现）：
y_1 = s1 - s2 - s3
print(f"第一句独有的词（没在第二、三句出现）：{y_1}")

# 三句都出现的词：
y_123 = s1 & s2 & s3
print(f"三句都出现的词：{y_123}")