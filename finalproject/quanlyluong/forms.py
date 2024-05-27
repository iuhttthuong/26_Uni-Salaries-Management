from django import forms
from .models import GIANGVIEN


class GiangVienForm(forms.ModelForm):
    GIOITINH_CHOICES = [
        ('Nam', 'Nam'),
        ('Nu', 'Nữ'),
    ]

    GIOITINH = forms.ChoiceField(
        choices=GIOITINH_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = GIANGVIEN
        fields = [
            'MAGIANGVIEN', 'MATD', 'HOTEN', 'NGAYSINH', 'GIOITINH',
            'SODIENTHOAI', 'DIACHI', 'MABAC', 'NGAYVAOLAM', 'CHUCVU', 'MANGACH', 'SOTIETDAY'
        ]

    def __init__(self, *args, **kwargs):
        super(GiangVienForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})

    def clean_GIOITINH(self):
        gioi_tinh = self.cleaned_data.get('GIOITINH')
        return True if gioi_tinh == 'Nam' else False
