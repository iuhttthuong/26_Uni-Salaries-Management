# import_data.py
import os
import django

# Thiết lập môi trường
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalproject.settings")
django.setup()

from quanlyluong.models import TRINHDO, CAPBAC, HESOLUONG, GIANGVIEN, TAIKHOAN
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
        {'MABAC': 'B1', 'TENBAC': 'Giảng viên'},
        {'MABAC': 'B2', 'TENBAC': 'Phó giáo sư'},
        {'MABAC': 'B3', 'TENBAC': 'Giáo sư'}
    ]

    for data in capbac_data:
        capbac, created = CAPBAC.objects.get_or_create(
            MABAC=data['MABAC'], defaults={'TENBAC': data['TENBAC']})
        print(f"Đã thêm: {data['TENBAC']}" if created else f"Đã tồn tại: {data['TENBAC']}")
        
def add_hesoluong():
    hesoluong_data = [
        {'MABAC': 'B1', 'HESO': 6.0},
        {'MABAC': 'B2', 'HESO': 1.2},
        {'MABAC': 'B3', 'HESO': 1.5}
    ]

    for data in hesoluong_data:
        capbac = CAPBAC.objects.get(MABAC=data['MABAC'])
        hesoluong, created = HESOLUONG.objects.get_or_create(
            MABAC=capbac, defaults={'HESO': data['HESO']})
        print(f"Đã thêm: {data['MABAC']} với hệ số {data['HESO']}" if created else f"Đã tồn tại: {data['MABAC']}")

def add_giangvien():
    giangvien_data = [
        {'MAGIANGVIEN': 1, 'MATD': 1, 'HOTEN': 'Nguyen Van A', 'NGAYSINH': '01-01-1980',
         'GIOITINH': bytes([1]), 'SODIENTHOAI': '0123456789', 'DIACHI': '123 Đường ABC', 'MABAC': 'B1',
         'NGAYVAOLAM': '01-01-2000', 'CHUCVU': 'GIANGVIEN'},
    ]

    for data in giangvien_data:
        trinhdo = TRINHDO.objects.get(MATD=data['MATD'])
        capbac = CAPBAC.objects.get(MABAC=data['MABAC'])
        giangvien, created = GIANGVIEN.objects.get_or_create(
            MAGIANGVIEN=data['MAGIANGVIEN'], defaults={'MATD': trinhdo, 'HOTEN': data['HOTEN'],
            'NGAYSINH': data['NGAYSINH'], 'GIOITINH': data['GIOITINH'], 'SODIENTHOAI': data['SODIENTHOAI'],
            'DIACHI': data['DIACHI'], 'MABAC': capbac, 'NGAYVAOLAM': data['NGAYVAOLAM'], 'CHUCVU': data['CHUCVU']})
        print(f"Đã thêm: {data['HOTEN']}" if created else f"Đã tồn tại: {data['HOTEN']}")

def add_taikhoan():
    taikhoan_data = [
        {'giang_vien_id': 1, 'MATKHAU': '1'},
    ]

    for data in taikhoan_data:
        giang_vien = GIANGVIEN.objects.get(MAGIANGVIEN=data['giang_vien_id'])
        taikhoan, created = TAIKHOAN.objects.get_or_create(
            giang_vien=giang_vien, defaults={'MATKHAU': data['MATKHAU']})
        print(f"Đã thêm tài khoản cho: {giang_vien.HOTEN}" if created else f"Đã tồn tại tài khoản cho: {giang_vien.HOTEN}")
        
def tinh_luong():
    giangvien = GIANGVIEN.objects.all()
    for gv in giangvien:
        hesoluong = HESOLUONG.objects.get(MABAC=gv.MABAC)
        luong = gv.MABAC.HESO.HESO * 1000000
        print(f"{gv.HOTEN} có mức lương: {luong}")

def main():
    add_trinhdo()
    add_capbac()
    add_hesoluong()
    add_giangvien()
    add_taikhoan()

if __name__ == "__main__":
    main()
