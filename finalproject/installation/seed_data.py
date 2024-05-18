# installation/seed_data.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalproject.settings')
django.setup()

from quanlyluong.models import TRINHDO, CAPBAC, NGACH, HESOLUONG, GIANGVIEN, TAIKHOAN

def seed_data():
    add_trinhdo()
    add_capbac()
    add_ngach()
    add_hesoluong()
    add_giangvien()
    add_taikhoan()

def add_trinhdo():
    trinhdo_data = [
        {'MATD': 1, 'TENTD': 'Cử nhân'},
        {'MATD': 2, 'TENTD': 'Thạc sĩ'},
        {'MATD': 3, 'TENTD': 'Tiến sĩ'}
    ]
    for data in trinhdo_data:
        TRINHDO.objects.get_or_create(MATD=data['MATD'], defaults={'TENTD': data['TENTD']})

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
        CAPBAC.objects.get_or_create(MABAC=data['MABAC'], defaults={'TENBAC': data['TENBAC']})

def add_ngach():
    ngach_data = [
        {'MANGACH': 'GVC', 'TENNGACH': 'Giảng Viên Chính'},
        {'MANGACH': 'GVTG', 'TENNGACH': 'Giảng Viên Và Trợ Giảng'},
        {'MANGACH': 'GVCC', 'TENNGACH': 'Giảng Viên Cao Cấp'}
    ]
    for data in ngach_data:
        NGACH.objects.get_or_create(MANGACH=data['MANGACH'], defaults={'TENNGACH': data['TENNGACH']})

def add_hesoluong():
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
        capbac = CAPBAC.objects.get(MABAC=data['MABAC'])
        HESOLUONG.objects.get_or_create(MANGACH=ngach, MABAC=capbac, defaults={'HESO': data['HESO']})

def add_giangvien():
    giangvien_data = [
        {
            'MAGIANGVIEN': '1',
            'MATD': 1,
            'MANGACH': 'GVCC',
            'HOTEN': 'Nguyen Van A',
            'NGAYSINH': '1980-01-01',
            'GIOITINH': True,
            'SODIENTHOAI': '0123456789',
            'DIACHI': '123 Đường ABC, Thành phố HCM',
            'MABAC': '1',
            'NGAYVAOLAM': '2000-01-01',
            'CHUCVU': 'GIANGVIEN'
        },
        {
            'MAGIANGVIEN': '2',
            'MATD': 2,
            'MANGACH': 'GVCC',
            'HOTEN': 'Nguyen Van B',
            'NGAYSINH': '1981-02-01',
            'GIOITINH': False,
            'SODIENTHOAI': '0987654321',
            'DIACHI': '456 Đường XYZ, Thành phố HN',
            'MABAC': '2',
            'NGAYVAOLAM': '2001-02-01',
            'CHUCVU': 'KETOAN'
        },
        {
            'MAGIANGVIEN': '3',
            'MATD': 1,
            'MANGACH': 'GVCC',
            'HOTEN': 'Nguyen Van C',
            'NGAYSINH': '1982-03-01',
            'GIOITINH': True,
            'SODIENTHOAI': '0123987654',
            'DIACHI': '789 Đường LMN, Thành phố ĐN',
            'MABAC': '3',
            'NGAYVAOLAM': '2002-03-01',
            'CHUCVU': 'HIEUTRUONG'
        },
    ]
    for data in giangvien_data:
        trinhdo = TRINHDO.objects.get(MATD=data['MATD'])
        ngach = NGACH.objects.get(MANGACH=data['MANGACH'])
        capbac = CAPBAC.objects.get(MABAC=data['MABAC'])
        GIANGVIEN.objects.get_or_create(
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

def add_taikhoan():
    taikhoan_data = [
        {'MAGIANGVIEN': '1', 'MATKHAU': '1'},
        {'MAGIANGVIEN': '2', 'MATKHAU': '1'},
        {'MAGIANGVIEN': '3', 'MATKHAU': '1'},
    ]

    for data in taikhoan_data:
        giangvien = GIANGVIEN.objects.get(MAGIANGVIEN=data['MAGIANGVIEN'])
        TAIKHOAN.objects.get_or_create(giang_vien=giangvien, defaults={'MATKHAU': data['MATKHAU']})


if __name__ == '__main__':
    print("Đang tạo dữ liệu...")
    seed_data()
    print("Hoàn thành!")