from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib import auth, messages

@login_required
def home(request):
 return render(request, "home.html", {})
def hieutruong(request):
    return render(request, 'hieutruong.html')
def adminas(request):
    return render(request, 'adminas.html')
def ketoan(request):
    return render(request, 'ketoan.html')
def giangvien(request):
    return render(request, 'giangvien.html')
def bangluong(request):
    return render(request, 'bangluong.html')
def authView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login details')
    return render(request, 'registration/login.html', {'form': LoginForm})
