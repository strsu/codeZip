# 이진수 변환
def binary(val):
    b = []
    while val > 0:
        if val % 2 == 1:
            b.append(1)
        else:
            b.append(0)
        val = val // 2
    return b

# 고속지수연산
def fastExpOp(a, exp, n):
    # a : 밑, exp : 지수, n : 모듈러 값
    x = binary(exp)
    y = 1
    for i, xi in enumerate(x):
        if xi == 1:
            y = (a * y) % n
        a = (a*a) % n
    return y

# 사용 - 11^22 mod 21 = 4
print(fastExpOp(11,22,21)) 
