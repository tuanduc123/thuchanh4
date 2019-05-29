a = input("Nhập các từ cách nhau bởi dấu cách trống: ").split()
dodai = len(a[0])
chuoi = a[0]
for i in a:
    if i.isspace():
        continue
    elif len(i) > dodai:
        dodai = len(i)
        chuoi = i
print(chuoi)