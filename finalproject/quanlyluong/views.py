from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import TAIKHOAN, GIANGVIEN, CAPBAC, HESOLUONG
from django.template import loader
from django.http import HttpResponse


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            tai_khoan = TAIKHOAN.objects.get(giang_vien_id=username)
            if password == tai_khoan.MATKHAU:
                request.session['user_id'] = username
                giang_vien = GIANGVIEN.objects.get(MAGIANGVIEN=username)
                messages.success(
                    request, f'Đăng nhập thành công. Chào mừng, {giang_vien.HOTEN}!')

                if giang_vien.CHUCVU == 'HIEUTRUONG':
                    # Trang chủ cho Hiệu Trưởng
                    return redirect('hieutruong_home')
                elif giang_vien.CHUCVU == 'GIANGVIEN':
                    # Trang chủ cho Giảng viên
                    return redirect('giangvien_home')
                elif giang_vien.CHUCVU == 'KETOAN':
                    # Trang chủ cho Kế toán
                    return redirect('emp_home')
                else:
                    # Chuyển hướng về trang đăng nhập nếu không có chức vụ hợp lệ
                    return redirect('login')

            else:
                messages.error(
                    request, 'Tên người dùng hoặc mật khẩu không đúng.')
        except TAIKHOAN.DoesNotExist:
            messages.error(request, 'Tên người dùng hoặc mật khẩu không đúng.')
    return render(request, 'login/loginpage.html')


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def emp_home(request):
    return render(request, 'login/emp_home.html')


def hieutruong_home(request):
    return render(request, 'login/hieutruong_home.html')


def giangvien_home(request):
    return render(request, 'login/giangvien_home.html')


def profile(request):
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        # Truy xuất thông tin giảng viên từ cơ sở dữ liệu
        giangvien = GIANGVIEN.objects.get(MAGIANGVIEN=user_id)
        return render(request, 'login/profile.html', {'giangvien': giangvien})
    else:
        # Nếu người dùng chưa đăng nhập, chuyển hướng đến trang đăng nhập
        return redirect('login/loginpage.html')


def hieutruong_profile(request):
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        # Truy xuất thông tin giảng viên từ cơ sở dữ liệu
        giangvien = GIANGVIEN.objects.get(MAGIANGVIEN=user_id)
        return render(request, 'login/hieutruong_profile.html', {'giangvien': giangvien})
    else:
        # Nếu người dùng chưa đăng nhập, chuyển hướng đến trang đăng nhập
        return redirect('login/loginpage.html')


def giangvien_profile(request):
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        # Truy xuất thông tin giảng viên từ cơ sở dữ liệu
        giangvien = GIANGVIEN.objects.get(MAGIANGVIEN=user_id)
        return render(request, 'login/giangvien_profile.html', {'giangvien': giangvien})
    else:
        # Nếu người dùng chưa đăng nhập, chuyển hướng đến trang đăng nhập
        return redirect('login/loginpage.html')


def search(request):
    giang_viens = None  # Đặt giang_viens là None hoặc một QuerySet rỗng
    query = request.GET.get('q')
    if query:  # Chỉ thực hiện truy vấn khi có giá trị 'q'
        giang_viens = GIANGVIEN.objects.filter(HOTEN__icontains=query)
    return render(request, 'login/search.html', {'giang_viens': giang_viens, 'query': query})


def hieutruong_search(request):
    giang_viens = None  # Đặt giang_viens là None hoặc một QuerySet rỗng
    query = request.GET.get('q')
    if query:  # Chỉ thực hiện truy vấn khi có giá trị 'q'
        giang_viens = GIANGVIEN.objects.filter(HOTEN__icontains=query)
    return render(request, 'login/hieutruong_search.html', {'giang_viens': giang_viens, 'query': query})


def view(request, magiangvien):
    giangvien = get_object_or_404(GIANGVIEN, MAGIANGVIEN=magiangvien)
    return render(request, 'login/view.html', {'giang_vien': giangvien})


def hieutruong_view(request, magiangvien):
    giangvien = get_object_or_404(GIANGVIEN, MAGIANGVIEN=magiangvien)
    return render(request, 'login/hieutruong_view.html', {'giang_vien': giangvien})


def update_salary(request, mabac):
    if request.method == 'POST':
        # Lặp qua các mục trong request.POST
        for key, value in request.POST.items():
            if key.startswith('hesoluong_'):
                mabac = key.split('_')[1]
                try:
                    hesoluong_record = HESOLUONG.objects.get(MABAC_id=mabac)
                    hesoluong_record.HESO = float(value)
                    hesoluong_record.save()
                    messages.success(request, 'Cập nhật thành công.')
                except HESOLUONG.DoesNotExist:
                    messages.error(request, 'Không tìm thấy hệ số lương.')
        return redirect('update_salary', mabac=mabac)
    else:
        teachers = GIANGVIEN.objects.filter(
            MABAC_id=mabac).select_related('MABAC')
        return render(request, 'login/update_salary.html', {'teachers': teachers})


def salary_slip(request, magiangvien):
    try:
        teacher = get_object_or_404(GIANGVIEN, pk=magiangvien)
        hesoluong = HESOLUONG.objects.get(MABAC=teacher.MABAC_id)
    except HESOLUONG.DoesNotExist:
        return HttpResponse("Salary coefficient not found for the provided instructor.", status=404)
    base_salary = 5000000
    calculated_salary = base_salary * hesoluong.HESO
    context = {
        'teacher': teacher,
        'base_salary': base_salary,
        'hesoluong': hesoluong.HESO,
        'calculated_salary': calculated_salary
    }
    return render(request, 'login/salary_slip.html', context)


def hieutruong_salary_slip(request, magiangvien):
    try:
        teacher = get_object_or_404(GIANGVIEN, pk=magiangvien)
        hesoluong = HESOLUONG.objects.get(MABAC=teacher.MABAC_id)
    except HESOLUONG.DoesNotExist:
        return HttpResponse("Salary coefficient not found for the provided instructor.", status=404)
    base_salary = 5000000
    calculated_salary = base_salary * hesoluong.HESO
    context = {
        'teacher': teacher,
        'base_salary': base_salary,
        'hesoluong': hesoluong.HESO,
        'calculated_salary': calculated_salary
    }
    return render(request, 'login/hieutruong_salary_slip.html', context)
