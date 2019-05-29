#Nhập một list từ bàn phím
ds = input("Nhap chuoi: ").split()
#Cắt list: lấy list nhưng bỏ phần đầu và cuối
x = ds[1:-1]
for c in x:
    print("Cắt list: ",x)
#Thêm phần tử vào list
ds.append('abc')
for ch in ds:
    print("Them phan tu abc: ",ch)
#Bỏ phàn tử khỏi list
ds.remove('123')
for ch in ds:
    print("Xoa phan tu 123: ",ch)
#Tìm kiếm phần tử trong list
print("Vi tri cua chuoi abc la: ",ds.index('abc'))
#Sắp xếp các phần tử trong list
ds.sort()
for ch in ds:
    print("Sap xep cac phan tu: ",ch)