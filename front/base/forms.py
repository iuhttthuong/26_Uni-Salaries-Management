from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Mã giảng viên", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
