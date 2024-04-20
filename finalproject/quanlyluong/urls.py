from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='quanlyluong'),
    path('emp_home/', views.emp_home, name='emp_home'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('view/<int:magiangvien>/', views.view, name='view'),
    path('update_salary/<str:mabac>/', views.update_salary, name='update_salary'),
    path('salary_slip/<int:magiangvien>/',
         views.salary_slip, name='salary_slip'),
    path('hieutruong_home/', views.hieutruong_home, name='hieutruong_home'),
    path('hieutruong_profile/', views.hieutruong_profile,
         name='hieutruong_profile'),
    path('hieutruong_search/', views.hieutruong_search, name='hieutruong_search'),
    path('hieutruong_view/<int:magiangvien>/',
         views.hieutruong_view, name='hieutruong_view'),
    path('hieutruong_salary_slip/<str:magiangvien>/',
         views.hieutruong_salary_slip, name='hieutruong_salary_slip'),
    path('giangvien_home/', views.giangvien_home, name='giangvien_home'),
    path('giangvien_profile/', views.giangvien_profile,
         name='giangvien_profile'),

]
