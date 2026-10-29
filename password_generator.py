import random
import string
CHAR_POOL = {
        "lower": string.ascii_lowercase,
        "upper": string.ascii_uppercase,
        "digit": string.digits,
        "symbol": "!@#$%^&*",
    }
def make_password(length, *kinds):
    """kinds 可以传入 "lower" / "upper" / "digit" / "symbol" 中的任意几个"""
    pool = ""
    for k in kinds:
        for p in k:
            pool += CHAR_POOL[p]
    while True:
        pw_list = []
        l,u,d,s = 0,0,0,0
        for i in range(int(length)):
            pw_list.append(random.choice(pool))
        if kinds_input == "1":
            break
        elif kinds_input == "2":
            for n in pw_list:
                if n in string.ascii_lowercase:
                    l += 1
                elif n in string.digits:
                    d += 1
            if l == 0 or d == 0:
                continue
            break
        elif kinds_input == "3":
            for n in pw_list:
                if n in string.ascii_lowercase:
                    l += 1
                elif n in string.ascii_uppercase:
                    u += 1
                elif n in string.digits:
                    d += 1
            if l == 0 or u == 0 or d == 0:
                continue
            break
        elif kinds_input == "4":
            for n in pw_list:
                if n in string.ascii_lowercase:
                    l += 1
                elif n in string.ascii_uppercase:
                    u += 1
                elif n in string.digits:
                    d += 1
                elif n in "!@#$%^&*":
                    s += 1
            if l == 0 or u == 0 or d == 0 or s == 0:
                continue
            break
    return "".join(pw_list)
while True:
    length_input = input("请输入密码长度（8-32）：").strip()
    if not length_input.isdigit():
        print(f"【{length_input}】请输入数字！")
        continue
    length = int(length_input)
    if length < 8 or length > 32:
        print(f"【{length}】超出范围（8—32）！")
        continue
    break
while True:
    kinds_input = input("请选择字符类型（1.仅小写  2.小写+数字  3.小写+大写+数字  4.全部）：")
    if kinds_input not in ("1", "2", "3", "4"):
        for m in kinds_input:
            if m not in string.digits:
                print(f"【{kinds_input}】字符类型输入错误！")
                break
            else:
                print(f"【{kinds_input}】字符类型无此选项！")
                break
        continue
    else:
        break
choices = {
    "1": ("lower",),
    "2": ("lower", "digit"),
    "3": ("lower", "upper", "digit"),
    "4": ("lower", "upper", "digit", "symbol"),
}
kinds = choices[kinds_input]
print(f"生成的密码：{make_password(length_input, kinds)}")