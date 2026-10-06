# #素材：
text = """  会议通知：请各位同学于 2026-10-05 前把材料发到 li_ming@example.com，抄送 zhang@school.edu.cn 一份。
            如有问题请联系 wang.hua@mail.com 或 phone@123（这个不是邮箱，请忽略）。
            补交材料请联系 li_ming@example.com，截止日期 2026-10-12。"""
#空列表测试
# text = "今天天气不错，没有邮箱。"

#任务1: 统计
#总字符数
#输出三个数字：总字符数：XX总单词数：XX总行数：XX
x = len(text)
print(f"总字符数：{x}")

#总单词数
# split() 将字符串按照指定字符串切割 - 列表
text_list1 = text.split()
#统计单词数不用循环  len() 字符串：字符数量 列表：里面有多少个元素
print(f"总单词数：{len(text_list1)}")

#总行数
# count() 统计子字符串在指定字符串中出现的次数
z = text.count("\n")
print(f"总行数：{z + 1}")

#任务2: 提取所有邮箱
mail = []
mail_num = 0
#改良过滤 re.split
# re.split 一次性切掉中文逗号、句号和空格
# 注意：切开后会产生空字符串，不过空串过不了邮箱检查，暂时不处理
import re
text_list2 = re.split("[，。 ]", text)

#开始提取邮箱及邮箱个数
for k in text_list2:
    if k.count("@") == 1:#含并且只含一个 @
        # find() 查找指定字符串第一次出现的索引位置
        if k.find("@") != 0:#@ 前面至少 1 个字符
            #rfind()：从右往左查找，找到最后一个匹配的下标
            # 【坑】这里两个点都要用 rfind。用 find 会取到第一个点，判断就错了
            if k.find("@") < k.rfind(".") and k.rfind(".") != len(k) - 1:#@ 后面要有一个 .，而且 . 不能在最后
                mail.append(k)
                mail_num += 1
print(f"此素材共有{mail_num}个邮箱，分别是{mail}")

# 任务3: 提取所有日期
# 判断标准：长度正好 10 个字符、第 5 位和第 8 位是 -、其余位是数字

#改良过滤 re.split
# re.split 一次性切掉中文逗号、句号和空格
# 注意：切开后会产生空字符串，不过空串过不了邮箱检查，暂时不处理
text_list3 = re.split("[，。 ]", text)

#开始提取日期及日期个数
date = []#日期
date_num = 0
for q in text_list3:
    if len(q) == 10:
        #find() 查找指定字符串第一次出现的索引位置 从左往右索引
        #rfind() 查找指定字符串最后一次出现的索引位置 从右往左索引
        if (q.find("-") == 4 and q.rfind("-") == 7
            #数字校验 isdigit() 字符串方法，判断字符串是不是全部由数字组成
                and q[:4].isdigit()
                and q[4] == "-"
                and q[5:7].isdigit()
                and q[7] == "-"
                and q[8:].isdigit()):
            date.append(q)
            date_num += 1
print(f"此素材共有{date_num}个日期，分别是{date}")










