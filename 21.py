S = input("Nhap chuoi nhi phan: ").split(',')
for i in S:
    if int(i, 2) % 5 == 0:
        print(i)
