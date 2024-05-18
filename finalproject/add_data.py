import csv
import os
import django

# Thiết lập môi trường
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalproject.settings")
django.setup()

from quanlyluong.models import TRINHDO, CAPBAC, HESOLUONG, GIANGVIEN, TAIKHOAN, NGACH

def load_csv_data(file_path):
    with open(file_path, encoding='utf-8') as csvfile:
        datareader = csv.DictReader(csvfile)
        return list(datareader)

def add_trinhdo(file_path):
    trinhdo_data = load_csv_data(file_path)
    for data in trinhdo_data:
        trinhdo, created = TRINHDO.objects.get_or_create(
            MATD=data['MATD'], defaults={'TENTD': data['TENTD']})
        if created:
            print(f"Thêm thành công trình độ: {data['TENTD']}")
        else:
            print(f"Trình độ đã tồn tại: {data['TENTD']}")

def add_capbac(file_path):
    capbac_data = load_csv_data(file_path)
    for data in capbac_data:
        capbac, created = CAPBAC.objects.get_or_create(
            MABAC=data['MABAC'], defaults={'TENBAC': data['TENBAC']})
        print(f"Đã thêm: {data['TENBAC']}" if created else f"Đã tồn tại: {data['TENBAC']}")

def add_ngach(file_path):
    ngach_data = load_csv_data(file_path)
    for data in ngach_data:
        ngach, created = NGACH.objects.get_or_create(
            MANGACH=data['MANGACH'], defaults={'TENNGACH': data['TENNGACH']})
        print(f"Đã thêm ngạch: {data['TENNGACH']}" if created else f"Ngạch đã tồn tại: {data['TENNGACH']}")

def add_hesoluong(file_path):
    hesoluong_data = load_csv_data(file_path)
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

def add_giangvien(file_path):
    giangvien_data = load_csv_data(file_path)
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
                'CHUCVU': data['CHUCVU'],
                'SOTIETDAY': data['SOTIETDAY']
            }
        )
        if created:
            print(f"Đã thêm giảng viên mới: {data['HOTEN']}")
        else:
            print(f"Giảng viên {data['HOTEN']} đã tồn tại.")

def add_taikhoan(file_path):
    taikhoan_data = load_csv_data(file_path)
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
    add_trinhdo('finalproject\\CSV_DATASET\\trinhdo.csv')
    add_capbac('finalproject\\CSV_DATASET\\capbac.csv')
    add_ngach('finalproject\\CSV_DATASET\\ngach.csv')
    add_hesoluong('finalproject\\CSV_DATASET\\hesoluong.csv')
    add_giangvien('finalproject\\CSV_DATASET\\giangvien.csv')
    add_taikhoan('finalproject\\CSV_DATASET\\taikhoan.csv')

if __name__ == "__main__":
    main()
