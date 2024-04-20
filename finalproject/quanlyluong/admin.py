from django.contrib import admin
from .models import TAIKHOAN, GIANGVIEN
# Register your models here.

# Register your models here.
# admin.site.register(TAIKHOAN)
admin.site.register((GIANGVIEN, TAIKHOAN))