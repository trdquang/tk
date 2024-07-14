#Kho hàng
hang_hoa = ['bút bi', 'tẩy', 'sách', 'thước kẻ']
gia = [10000, 5000, 15000, 5000]

#khai báo menu
lua_chon = -1
menu = '''
CHÀO MỪNG BẠN ĐẾN VỚI CỬA HÀNG ĐỒ DÙNG HỌC TẬP
HÃY NHẬP LỤA CHỌN CỦA BẠN
1. Mua bút bi (10.000 vnđ)
2. Mua tẩy (5.000 vnđ)
3. Mua sách (15.000 vnđ)
4. Mua thước kẻ (5.000 vnđ)
0. Kết thúc mua hàng
'''

#giỏ hàng lưu số lượng các món hàng
gio_hang = [0, 0, 0, 0]
tong_tien = 0

print(menu)
ho_ten_khach = input('Tên quý khách: ')
dia_chi_khach = input('Địa chỉ: ')
while lua_chon != 0:
    lua_chon = int(input('Lựa chọn của bạn : '))

    if lua_chon >=1 and lua_chon <= 4:
        index = lua_chon - 1
        so_luong = int(input('nhập số lượng ' + hang_hoa[index] + ' muốn mua: '))
        gio_hang[index] += so_luong
        tong_tien += gia[index] * so_luong
        print('----------------đã thêm thành công. Xin mời tiếp tục !----------------')
        
    elif lua_chon == 0:
        print('\n\tCảm ơn quý khách đã mua hàng')
        print('Thông tin hóa đơn')
        print('Khách: ' + ho_ten_khach, end = '')
        print('\tĐịa chỉ: ' + dia_chi_khach)
        print('Giỏ hàng')
        for i in range(0, len(hang_hoa)):
            if gio_hang[i] != 0:
              print(hang_hoa[i] + ': ' + str(gio_hang[i]))
        print('Tổng tiền: ' + str(tong_tien) + '(vnd)')
        break
        
        
    
