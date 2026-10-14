#练遍历、get()、items()

# 第 1 题 · 打印库存清单
stock = {"苹果": 12, "香蕉": 0, "橘子": 7, "葡萄": 3}
# 要求输出
# ---------- 库存 ----------
# 苹果：12 个
# 香蕉：0 个   ⚠️ 缺货
# 橘子：7 个
# 葡萄：3 个
# --------------------------
print("---------- 库存 ----------")
for name,num in stock.items():
    if num == 0:
        print(f"{name} : {num} 个   ⚠️ 缺货")
    else:
        print(f"{name} : {num} 个")
print("--------------------------")

#第 2 题 · 查价格
# 场景：用户输入商品名查价格。输入的东西是不可信的——他可能打错字。
price = {"苹果": 5.5, "香蕉": 3.0, "橘子": 4.2}
# 要求：
# 请输入商品名：苹果
# 苹果 的价格是 5.5 元
#
# 请输入商品名：西瓜
# ⚠️ 没有「西瓜」这个商品
name = input("请输入商品名：")
# if price.get(name) is None:
#     print(f"⚠️ 没有「{name}」这个商品")
# else:
#     print(f"{name} 的价格是 {price.get(name)} 元")
#功能没问题，但同一个值查了两次。 存一次更干净：
p = price.get(name)
if p is None:
    print(f"⚠️ 没有「{name}」这个商品")
else:
    print(f"{name} 的价格是 {p} 元")

# 第 3 题 · 词频统计
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# 要求输出：
# apple：3 次
# banana：2 次
# cherry：1 次
words_dict = {}
for i in words:
    # if i in words_dict:
    #     words_dict[i] += 1
    # else:
    #     words_dict[i] = 1
    # 但.get()
    # 就是为这个场景设计的——四行变一行：
    words_dict[i] = words_dict.get(i, 0) + 1 # get()能给不存在的键一个起点值。
for name,num in words_dict.items():
    print(f"{name} : {num} 次")

# 第 4 题 · 合并两个购物车
cart1 = {"苹果": 3, "香蕉": 2}
cart2 = {"香蕉": 5, "橘子": 1}
# 要求输出（同名商品数量相加）：
# {'苹果': 3, '香蕉': 7, '橘子': 1}
# cart = cart1   !!!Python 里这样写，cart 和 cart1 指向的是同一个字典。 改 cart 就等于改 cart1
cart = cart1.copy()      # 真正独立的副本
for name,num in cart2.items():
    if name in cart:
        cart[name] += num
    else:
        cart[name] = num
print(f"{cart}")