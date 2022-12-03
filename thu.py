# #y = ['47%','GIẢM','Tài Trợ','Áo Thun Polo Nam Sọc Ngang cổ bẻ ; vải Poly Cá Sấu Cao Cấp Chuẩn Form','50% Giảm','₫300.000','₫160.000','TP. Hồ Chí Minh']
# #y = ['15%','GIẢM','Tài Trợ','Áo Thun Polo Trơn Nam SUTU Phong Cách Basic Đơn Giản Phù Hợp Với Tất Cả Mọi Người A08DES','Giảm ₫35k','₫320.000','₫272.000','Đã bán 61','TP. Hồ Chí Minh']
# y = ['Tài Trợ','Áo Thun Nam Polo PACK MAN; Cotton Cá Sấu; mát mịn; Ngắn Tay','50% Giảm','₫230.000','Bình Dương']


# #tinh 
# print(y[-1])

# #đã bán
# #print(y[-2])

# y_string = str(y)
# vi_tri_dau = y_string.find('Đã bán')
# if vi_tri_dau != -1:
# # -1 if the value is not found.
# 	sold = y_string[int(vi_tri_dau)+7:int(vi_tri_dau)+11]
# 	print('da ban: ',sold)
# 	print('gia la:',y[-3])
# else:
# 	print('gia la:',y[-2])


# #giá
# # y_string = str(y)
# # vi_tri_dau = y_string.find('₫')
# # vi_tri_cuoi = y_string.find('.000')
# # sold = y_string[int(vi_tri_cuoi)-3:int(vi_tri_cuoi)]
# # print(sold)

# # vi_tri_cuoi_1 = y_string.find('.000')
# # sold_1 = y_string[int(vi_tri_cuoi)-3:int(vi_tri_cuoi)]
# # print(sold_1)

# #tên
# max_lenght = 0
# name = ''
# for i in y:
# 	if len(i) > max_lenght:
# 		max_lenght = len(i)
# 		name = i 

# print(name)
# # print(y[-6])


y = ['162']
x = str(y)
z = int(x)
print(z)