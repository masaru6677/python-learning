#阶乘 (递归)
def jc(n):
    if n == 1 or n == 0:
        return 1
    elif n <= 0:
        raise ValueError("n 不能小于 0")
    else:
        return n * jc(n-1)
print(jc(-1))

#斐波那契 (递归)
def fibonacci(n, a=1, b=1):
    """返回前 n 个斐波那契数，用空格连接"""
    if n <= 0:
        return ""
    if n == 1:
        return str(a)
    if n == 2:
        return f"{a} {b}"
    return f"{a} {b} " + fibonacci(n - 2, a + b, b + a + b)
print(fibonacci(5,1,1))
print(fibonacci(6,1,1))
print(fibonacci(7,1,1))

# 【坑】之前把 n == 1 当边界，jc(0) 会一路递归到负数 → RecursionError
# 【坑】之前用全局 sequence 收集结果，第二次调用就把列表污染了 → 改成靠返回值