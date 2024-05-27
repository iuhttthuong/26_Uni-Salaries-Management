from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import TAIKHOAN, GIANGVIEN, CAPBAC, HESOLUONG
from django.template import loader
from django.http import HttpResponse
import re


def login_hieutruong(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            tai_khoan = TAIKHOAN.objects.get(giang_vien_id=username)
            if password == tai_khoan.MATKHAU and tai_khoan.giang_vien.CHUCVU == 'HIEUTRUONG':
                request.session['user_id'] = username
                messages.success(
                    request, f'Đăng nhập thành công. Chào mừng, {tai_khoan.giang_vien.HOTEN}!')
                return redirect('hieutruong_home')
            else:
                messages.error(
                    request, 'Lỗi đăng nhập')
        except TAIKHOAN.DoesNotExist:
            messages.error(request, 'Tên người dùng hoặc mật khẩu không đúng.')
    return render(request, 'login/login_hieutruong.html')


def login_giangvien(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            tai_khoan = TAIKHOAN.objects.get(giang_vien_id=username)
            if password == tai_khoan.MATKHAU and tai_khoan.giang_vien.CHUCVU == 'GIANGVIEN':
                request.session['user_id'] = username
                messages.success(
                    request, f'Đăng nhập thành công. Chào mừng, {tai_khoan.giang_vien.HOTEN}!')
                return redirect('giangvien_home')
            else:
                messages.error(
                    request, 'Lỗi đăng nhập')
        except TAIKHOAN.DoesNotExist:
            messages.error(request, 'Tên người dùng hoặc mật khẩu không đúng.')
    return render(request, 'login/login_giangvien.html')


def login_ketoan(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            tai_khoan = TAIKHOAN.objects.get(giang_vien_id=username)
            if password == tai_khoan.MATKHAU and tai_khoan.giang_vien.CHUCVU == 'KETOAN':
                request.session['user_id'] = username
                messages.success(
                    request, f'Đăng nhập thành công. Chào mừng, {tai_khoan.giang_vien.HOTEN}!')
                return redirect('emp_home')
            else:
                messages.error(
                    request, 'Lỗi đăng nhập')
        except TAIKHOAN.DoesNotExist:
            messages.error(request, 'Tên người dùng hoặc mật khẩu không đúng.')
    return render(request, 'login/login_ketoan.html')


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


def giangvien_search(request):
    giang_viens = None  # Đặt giang_viens là None hoặc một QuerySet rỗng
    query = request.GET.get('q')
    if query:  # Chỉ thực hiện truy vấn khi có giá trị 'q'
        giang_viens = GIANGVIEN.objects.filter(HOTEN__icontains=query)
    return render(request, 'login/giangvien_search.html', {'giang_viens': giang_viens, 'query': query})


def hieutruong_search(request):
    giang_viens = None  # Đặt giang_viens là None hoặc một QuerySet rỗng
    query = request.GET.get('q')
    if query:  # Chỉ thực hiện truy vấn khi có giá trị 'q'
        giang_viens = GIANGVIEN.objects.filter(HOTEN__icontains=query)
    return render(request, 'login/hieutruong_search.html', {'giang_viens': giang_viens, 'query': query})


def view(request, magiangvien):
    giangvien = get_object_or_404(GIANGVIEN, MAGIANGVIEN=magiangvien)
    return render(request, 'login/view.html', {'giang_vien': giangvien})


def giangvien_view(request, magiangvien):
    giangvien = get_object_or_404(GIANGVIEN, MAGIANGVIEN=magiangvien)
    return render(request, 'login/giangvien_view.html', {'giang_vien': giangvien})


def hieutruong_view(request, magiangvien):
    giangvien = get_object_or_404(GIANGVIEN, MAGIANGVIEN=magiangvien)
    return render(request, 'login/hieutruong_view.html', {'giang_vien': giangvien})


def update_salary1(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('heso_'):
                try:
                    id = int(key.split('_')[1])
                    heso_luong = HESOLUONG.objects.get(id=id)
                    heso_luong.HESO = float(value)
                    heso_luong.save()
                except (HESOLUONG.DoesNotExist, ValueError) as e:
                    print(e)

    luongs = HESOLUONG.objects.all()

    # Extract values inside parentheses for both MANGACH and MABAC
    for luong in luongs:
        mangach_match = re.search(r'\((.*?)\)', str(luong.MANGACH))
        mabac_match = re.search(r'\((.*?)\)', str(luong.MABAC))

        luong.MANGACH_paren = mangach_match.group(1) if mangach_match else ''
        luong.MABAC_paren = mabac_match.group(1) if mabac_match else ''

    return render(request, 'login/update_salary1.html', {'luongs': luongs, 'message': 'Cập nhật thành công.'})

def salary_slip(request, magiangvien, sotietdaytoithieu = 50,luongtheogio = 24500):
    try:
        teacher = get_object_or_404(GIANGVIEN, pk=magiangvien)
        hesoluong = HESOLUONG.objects.get(
            MABAC=teacher.MABAC_id, MANGACH=teacher.MANGACH_id)
    except HESOLUONG.DoesNotExist:
        return HttpResponse("Salary coefficient not found for the provided instructor.", status=404)
    base_salary = 1800000
    calculated_salaryM = base_salary * hesoluong.HESO
    calculated_salaryY = base_salary * hesoluong.HESO * 12 +(teacher.SOTIETDAY - sotietdaytoithieu) * luongtheogio
    context = {
        'teacher': teacher,
        'base_salary': base_salary,
        'hesoluong': hesoluong.HESO,
        'calculated_salaryM': calculated_salaryM,
        'calculated_salaryY': calculated_salaryY,
        'final_salary': calculated_salaryY + calculated_salaryY*0.3 - calculated_salaryY*0.105
    }
    return render(request, 'login/salary_slip.html', context)


def hieutruong_salary_slip(request, magiangvien, sotietdaytoithieu = 50,luongtheogio = 24500):
    try:
        teacher = get_object_or_404(GIANGVIEN, pk=magiangvien)
        hesoluong = HESOLUONG.objects.get(
            MABAC=teacher.MABAC_id, MANGACH=teacher.MANGACH_id)
        base_salary = 1800000
        calculated_salaryM = base_salary * hesoluong.HESO
        calculated_salaryY = base_salary * hesoluong.HESO * 12 +(teacher.SOTIETDAY - sotietdaytoithieu) * luongtheogio
        context = {
            'teacher': teacher,
            'base_salary': base_salary,
            'hesoluong': hesoluong.HESO,
            'calculated_salaryM': calculated_salaryM,
            'calculated_salaryY': calculated_salaryY,
            'final_salary': calculated_salaryY + calculated_salaryY*0.3 - calculated_salaryY*0.105
        }
        return render(request, 'login/hieutruong_salary_slip.html', context)
    except HESOLUONG.DoesNotExist:
        return HttpResponse("Salary coefficient not found for the provided instructor.", status=404)
    except HESOLUONG.MultipleObjectsReturned:
        return HttpResponse("Data inconsistency error.", status=500)

def hieutruong_update(request, magiangvien):
    teacher = get_object_or_404(GIANGVIEN, MAGIANGVIEN=magiangvien)
    
    if request.method == 'POST':
        teacher.HOTEN = request.POST.get(f'hoten_{teacher.MAGIANGVIEN}', teacher.HOTEN)
        teacher.NGAYSINH = request.POST.get(f'ngaysinh_{teacher.MAGIANGVIEN}', teacher.NGAYSINH)
        teacher.GIOITINH = request.POST.get(f'gioitinh_{teacher.MAGIANGVIEN}', teacher.GIOITINH)
        teacher.SODIENTHOAI = request.POST.get(f'sodienthoai_{teacher.MAGIANGVIEN}', teacher.SODIENTHOAI)
        teacher.DIACHI = request.POST.get(f'diachi_{teacher.MAGIANGVIEN}', teacher.DIACHI)
        teacher.NGAYVAOLAM = request.POST.get(f'ngayvaolam_{teacher.MAGIANGVIEN}', teacher.NGAYVAOLAM)
        teacher.CHUCVU = request.POST.get(f'chucvu_{teacher.MAGIANGVIEN}', teacher.CHUCVU)
        teacher.SOTIETDAY = request.POST.get(f'sotietday_{teacher.MAGIANGVIEN}', teacher.SOTIETDAY)
        teacher.MABAC_id = request.POST.get(f'mabac_{teacher.MAGIANGVIEN}', teacher.MABAC_id)
        teacher.MANGACH_id = request.POST.get(f'mangach_{teacher.MAGIANGVIEN}', teacher.MANGACH_id)
        teacher.MATD_id = request.POST.get(f'matd_{teacher.MAGIANGVIEN}', teacher.MATD_id)
        teacher.save()
        return render(request, 'login/hieutruong_view.html', {'giang_vien': teacher})

    return render(request, 'login/hieutruong_update.html', {'teacher': teacher})


def logout_giangvien(request):
    # Kiểm tra xem session 'user_id' có tồn tại không
    if 'user_id' in request.session:
        # Xóa 'user_id' khỏi session
        del request.session['user_id']
        # Gửi thông báo đăng xuất thành công
        messages.success(request, 'Bạn đã đăng xuất thành công.')
    else:
        # Gửi thông báo người dùng không đăng nhập
        messages.error(request, 'Bạn chưa đăng nhập.')

    # Chuyển hướng đến trang đăng nhập
    return render(request, 'login/login_giangvien.html')


def logout_ketoan(request):
    # Kiểm tra xem session 'user_id' có tồn tại không
    if 'user_id' in request.session:
        # Xóa 'user_id' khỏi session
        del request.session['user_id']
        # Gửi thông báo đăng xuất thành công
        messages.success(request, 'Bạn đã đăng xuất thành công.')
    else:
        # Gửi thông báo người dùng không đăng nhập
        messages.error(request, 'Bạn chưa đăng nhập.')

    # Chuyển hướng đến trang đăng nhập
    return render(request, 'login/login_ketoan.html')


def logout_hieutruong(request):
    # Kiểm tra xem session 'user_id' có tồn tại không
    if 'user_id' in request.session:
        # Xóa 'user_id' khỏi session
        del request.session['user_id']
        # Gửi thông báo đăng xuất thành công
        messages.success(request, 'Bạn đã đăng xuất thành công.')
    else:
        # Gửi thông báo người dùng không đăng nhập
        messages.error(request, 'Bạn chưa đăng nhập.')

    # Chuyển hướng đến trang đăng nhập
    return render(request, 'login/login_hieutruong.html')
