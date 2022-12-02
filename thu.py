y = ['2%','GIẢM','Tài Trợ','[Mã FATREND1 giảm 8% đơn 99K] Áo thun POLO nam BASIC Quality CVC mềm mịn; thoáng mát cùng công nghệ Cool-SM IVATNAM','10% Giảm','Mua 2 & giảm 5%','₫365.000','₫359.000','Đã bán 249','Hà Nội']

#['15%','GIẢM','Tài Trợ','Áo Thun Polo Trơn Nam SUTU Phong Cách Basic Đơn Giản Phù Hợp Với Tất Cả Mọi Người A08DES','Giảm ₫35k','₫320.000','₫272.000','Đã bán 61','TP. Hồ Chí Minh']

#tinh 
print(y[-1])

#đã bán
print(y[-2])

#giá
print(y[-3])

#tên
max_lenght = 0
name = ''
for i in y:
	if len(i) > max_lenght:
		max_lenght = len(i)
		name = i 

print(name)
# print(y[-6])
