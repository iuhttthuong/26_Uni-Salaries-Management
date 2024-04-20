import os
import django

# Thiết lập môi trường
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalproject.settings")
django.setup()

from quanlyluong.models import TRINHDO, CAPBAC, HESOLUONG, GIANGVIEN, TAIKHOAN, NGACH

def add_trinhdo():
    trinhdo_data = [
        {'MATD': 1, 'TENTD': 'Cử nhân'},
        {'MATD': 2, 'TENTD': 'Thạc sĩ'},
        {'MATD': 3, 'TENTD': 'Tiến sĩ'}
    ]

    for data in trinhdo_data:
        trinhdo, created = TRINHDO.objects.get_or_create(
            MATD=data['MATD'], defaults={'TENTD': data['TENTD']})
        if created:
            print(f"Thêm thành công trình độ: {data['TENTD']}")
        else:
            print(f"Trình độ đã tồn tại: {data['TENTD']}")

def add_capbac():
    capbac_data = [
        {'MABAC': '1', 'TENBAC': 'Bậc 1'},
        {'MABAC': '2', 'TENBAC': 'Bậc 2'},
        {'MABAC': '3', 'TENBAC': 'Bậc 3'},
        {'MABAC': '4', 'TENBAC': 'Bậc 4'},
        {'MABAC': '5', 'TENBAC': 'Bậc 5'},
        {'MABAC': '6', 'TENBAC': 'Bậc 6'},
        {'MABAC': '7', 'TENBAC': 'Bậc 7'},
        {'MABAC': '8', 'TENBAC': 'Bậc 8'}
    ]

    for data in capbac_data:
        capbac, created = CAPBAC.objects.get_or_create(
            MABAC=data['MABAC'], defaults={'TENBAC': data['TENBAC']})
        print(f"Đã thêm: {data['TENBAC']}" if created else f"Đã tồn tại: {data['TENBAC']}")

def add_ngach():
    ngach_data = [
        {'MANGACH': 'GVC', 'TENNGACH': 'Giảng Viên Chính'},
        {'MANGACH': 'GVTG', 'TENNGACH': 'Giảng Viên Và Vrợ Giảng'},
        {'MANGACH': 'GVCC', 'TENNGACH': 'Giảng Ciên Cao Cấp'}
    ]

    for data in ngach_data:
        ngach, created = NGACH.objects.get_or_create(
            MANGACH=data['MANGACH'], defaults={'TENNGACH': data['TENNGACH']})
        print(f"Đã thêm ngạch: {data['TENNGACH']}" if created else f"Ngạch đã tồn tại: {data['TENNGACH']}")

def add_hesoluong():# Hoàn thiện dữ liệu với các bậc và hệ số lương giả định cho từng ngạch
    hesoluong_data = [
        
        {'MANGACH': 'GVC', 'MABAC': '1', 'HESO': 4.40},
        {'MANGACH': 'GVC', 'MABAC': '2', 'HESO': 4.47},
        {'MANGACH': 'GVC', 'MABAC': '3', 'HESO': 5.08},
        {'MANGACH': 'GVC', 'MABAC': '4', 'HESO': 5.42},
        {'MANGACH': 'GVC', 'MABAC': '5', 'HESO': 5.76},
        {'MANGACH': 'GVC', 'MABAC': '6', 'HESO': 6.10},
        {'MANGACH': 'GVC', 'MABAC': '7', 'HESO': 6.44},
        {'MANGACH': 'GVC', 'MABAC': '8', 'HESO': 6.78},

        {'MANGACH': 'GVTG', 'MABAC': '1', 'HESO': 2.34},
        {'MANGACH': 'GVTG', 'MABAC': '2', 'HESO': 2.67},
        {'MANGACH': 'GVTG', 'MABAC': '3', 'HESO': 3},
        {'MANGACH': 'GVTG', 'MABAC': '4', 'HESO': 3.33},
        {'MANGACH': 'GVTG', 'MABAC': '5', 'HESO': 3.66},
        {'MANGACH': 'GVTG', 'MABAC': '6', 'HESO': 3.99},
        {'MANGACH': 'GVTG', 'MABAC': '7', 'HESO': 4.32},
        {'MANGACH': 'GVTG', 'MABAC': '8', 'HESO': 4.65},


        {'MANGACH': 'GVCC', 'MABAC': '1', 'HESO': 6.20},
        {'MANGACH': 'GVCC', 'MABAC': '2', 'HESO': 6.56},
        {'MANGACH': 'GVCC', 'MABAC': '3', 'HESO': 6.92},
        {'MANGACH': 'GVCC', 'MABAC': '4', 'HESO': 7.28},
        {'MANGACH': 'GVCC', 'MABAC': '5', 'HESO': 7.64},
        {'MANGACH': 'GVCC', 'MABAC': '6', 'HESO': 8.00},
    ]

    for data in hesoluong_data:
        ngach = NGACH.objects.get(MANGACH=data['MANGACH'])
        capbac, cb_created = CAPBAC.objects.get_or_create(MABAC=data['MABAC'])
        hesoluong, hs_created = HESOLUONG.objects.get_or_create(
            MANGACH=ngach, MABAC=capbac, defaults={'HESO': data['HESO']})
        
        if hs_created:
            print(f"Đã thêm hệ số lương mới: {data['HESO']} cho ngạch {data['MANGACH']} bậc {data['MABAC']}")
        else:
            hesoluong.HESO = data['HESO']
            hesoluong.save()
            print(f"Cập nhật hệ số lương: {data['HESO']} cho ngạch {data['MANGACH']} bậc {data['MABAC']}")

def add_giangvien():
    
    giangvien_data = [
        {
            'MAGIANGVIEN': '1',
            'MATD': 1,  # Giả định trình độ này đã được thêm trong bảng TRINHDO
            'MANGACH': 'GVCC',  # Giả định ngạch này đã được thêm trong bảng NGACH
            'HOTEN': 'Nguyen Van A',
            'NGAYSINH': '1980-01-01',
            'GIOITINH': True,  # Giả sử True là nam và False là nữ
            'SODIENTHOAI': '0123456789',
            'DIACHI': '123 Đường ABC, Thành phố HCM',
            'MABAC': '1',  # Giả định bậc này đã được thêm trong bảng CAPBAC
            'NGAYVAOLAM': '2000-01-01',
            'CHUCVU': 'GIANGVIEN'
        },
        {
            'MAGIANGVIEN': '2',
            'MATD': 2,  # Giả định trình độ này đã được thêm trong bảng TRINHDO
            'MANGACH': 'GVCC',  # Giả định ngạch này đã được thêm trong bảng NGACH
            'HOTEN': 'Nguyen Van A',
            'NGAYSINH': '1980-01-01',
            'GIOITINH': True,  # Giả sử True là nam và False là nữ
            'SODIENTHOAI': '0123456789',
            'DIACHI': '123 Đường ABC, Thành phố HCM',
            'MABAC': '1',  # Giả định bậc này đã được thêm trong bảng CAPBAC
            'NGAYVAOLAM': '2000-01-01',
            'CHUCVU': 'KETOAN'
        },
        {
            'MAGIANGVIEN': '3',
            'MATD': 1,  # Giả định trình độ này đã được thêm trong bảng TRINHDO
            'MANGACH': 'GVCC',  # Giả định ngạch này đã được thêm trong bảng NGACH
            'HOTEN': 'Nguyen Van A',
            'NGAYSINH': '1980-01-01',
            'GIOITINH': True,  # Giả sử True là nam và False là nữ
            'SODIENTHOAI': '0123456789',
            'DIACHI': '123 Đường ABC, Thành phố HCM',
            'MABAC': '1',  # Giả định bậc này đã được thêm trong bảng CAPBAC
            'NGAYVAOLAM': '2000-01-01',
            'CHUCVU': 'HIEUTRUONG'
        },
    ]

    for data in giangvien_data:
        trinhdo = TRINHDO.objects.get(MATD=data['MATD'])
        ngach = NGACH.objects.get(MANGACH=data['MANGACH'])
        capbac = CAPBAC.objects.get(MABAC=data['MABAC'])
        giangvien, created = GIANGVIEN.objects.get_or_create(
            MAGIANGVIEN=data['MAGIANGVIEN'],
            defaults={
                'MATD': trinhdo,
                'MANGACH': ngach,
                'HOTEN': data['HOTEN'],
                'NGAYSINH': data['NGAYSINH'],
                'GIOITINH': data['GIOITINH'],
                'SODIENTHOAI': data['SODIENTHOAI'],
                'DIACHI': data['DIACHI'],
                'MABAC': capbac,
                'NGAYVAOLAM': data['NGAYVAOLAM'],
                'CHUCVU': data['CHUCVU']
            }
        )
        if created:
            print(f"Đã thêm giảng viên mới: {data['HOTEN']}")
        else:
            print(f"Giảng viên {data['HOTEN']} đã tồn tại.")

def add_taikhoan():
    taikhoan_data = [
        {'MAGIANGVIEN': '1', 'MATKHAU': '1'},
        {'MAGIANGVIEN': '2', 'MATKHAU': '1'},
        {'MAGIANGVIEN': '3', 'MATKHAU': '1'},
    ]

    for data in taikhoan_data:
        giangvien = GIANGVIEN.objects.get(MAGIANGVIEN=data['MAGIANGVIEN'])
        taikhoan, created = TAIKHOAN.objects.get_or_create(
            giang_vien=giangvien,
            defaults={'MATKHAU': data['MATKHAU']}
        )
        if created:
            print(f"Đã tạo tài khoản cho giảng viên: {giangvien.HOTEN}")
        else:
            print(f"Tài khoản cho giảng viên {giangvien.HOTEN} đã tồn tại.")

def main():
    add_trinhdo()
    add_capbac()
    add_ngach()
    add_hesoluong()
    add_giangvien()
    add_taikhoan()

if __name__ == "__main__":
    main()
