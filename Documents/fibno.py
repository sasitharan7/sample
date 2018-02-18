def finbo(number):
    a = 1
    b = 1
    out = []
    for i in range(number):
        out.append(a)
        a,b = b, a+b
    return out
print(finbo(10))

