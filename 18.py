a, b = 0, 1
n = int(input("Nhập giá trị n: "))
while b < n:
    a, b = b, a + b
    print(a)