# Lambda function

# def x(a):
#     return a * 2

# y = lambda a : a * 2

# print(x(2))
# print(y(3))


# def x(a,b,c):
#     return a + b + c

# y = lambda a,b,c : a + b + c

# # print(x(1,2,3))
# # print(y(1,2,3))

# def kali(n):
#     return lambda x : x * n

# kaliDua = kali(2)
# kaliTiga = kali(3)

# print(kaliDua(11))
# print(kaliTiga(11))


def y(a):
    return a
def x(a):
    print(y(a))
x(12)

def z():
    return lambda c : c
b = z()
print(b(13))