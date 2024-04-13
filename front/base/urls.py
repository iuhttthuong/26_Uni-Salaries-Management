from django.urls import path, include
from .views import authView, home
from .views import hieutruong
from .views import adminas
from .views import ketoan
from .views import giangvien
from .views import bangluong
urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('hieutruong/', hieutruong, name='hieutruong'),
    path('adminas/', adminas, name='adminas'),
    path('ketoan/', ketoan, name='ketoan'),
    path('giangvien/', giangvien, name='giangvien'),
    path('bangluong/', bangluong, name='bangluong'),
]