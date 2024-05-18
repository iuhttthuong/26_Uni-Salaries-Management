from django.db import models

# Create your models here.
    
# Bảng dữ liệu TRÌNH ĐỘ
class TRINHDO(models.Model):
    MATD = models.IntegerField(primary_key = True) # Mã trình độ
    TENTD = models.CharField(max_length=50) # Tên trình độ

# Bảng dữ liệu CẤP BẬC
class CAPBAC(models.Model):
    MABAC = models.CharField(max_length=10, primary_key=True) # Mã bậc
    TENBAC = models.CharField(max_length=50) # Tên bậc

class NGACH(models.Model):
    MANGACH = models.CharField(max_length=10, primary_key=True)  # Mã ngạch
    TENNGACH = models.CharField(max_length=50)  # Tên ngạch
    
# Bảng dữ liệu HỆ SỐ LƯƠNG
class HESOLUONG(models.Model):
    MABAC = models.ForeignKey(CAPBAC, on_delete=models.CASCADE)
    MANGACH = models.ForeignKey(NGACH, on_delete=models.CASCADE)
    HESO = models.FloatField()

    class Meta:
        unique_together = (('MABAC', 'MANGACH'),)  # Khóa chính composite
        verbose_name_plural = "Hệ số lương"

# Bảng dữ liệu GIẢNG VIÊN
class GIANGVIEN(models.Model):
    MAGIANGVIEN = models.CharField(max_length= 8, primary_key=True, unique=True)
    MATD = models.ForeignKey(TRINHDO, on_delete=models.CASCADE) #Mã trình độ
    HOTEN = models.CharField(max_length=50)
    NGAYSINH = models.CharField(max_length=10)    
    GIOITINH = models.BooleanField()
    SODIENTHOAI = models.CharField(max_length=10)
    DIACHI = models.CharField(max_length=100)
    MABAC = models.ForeignKey(CAPBAC, on_delete=models.CASCADE) #Mã bậc
    NGAYVAOLAM = models.CharField(max_length=10)    
    CHUCVU = models.CharField(max_length=50)
    MANGACH = models.ForeignKey(NGACH, on_delete=models.CASCADE) 
    SOTIETDAY = models.IntegerField()
    
class TAIKHOAN(models.Model):
    giang_vien = models.OneToOneField(GIANGVIEN, on_delete=models.CASCADE, primary_key=True)
    MATKHAU = models.CharField(max_length=50) 