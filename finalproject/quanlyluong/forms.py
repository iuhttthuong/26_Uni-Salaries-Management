from django import forms
from .models import GIANGVIEN, TRINHDO,CAPBAC,NGACH

class GiangVienForm(forms.ModelForm):
    GIOITINH_CHOICES = [
        ('Nam', 'Nam'),
        ('Nu', 'Nữ'),
    ]
    CHUCVU_CHOICES = [
        ('GIANGVIEN', 'Giảng viên'),
        ('KETOAN', 'Nhân Viên'),
    ]
    CHUCVU = forms.ChoiceField(
        choices=CHUCVU_CHOICES, widget=forms.Select)
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
        # Lấy danh sách MATD từ TRINHDO
        self.fields['MATD'].choices = [(td.MATD, td.TENTD) for td in TRINHDO.objects.all()]
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})
        # Lấy danh sách MABAC từ CAPBAC
        self.fields['MABAC'].choices = [(bac.MABAC, bac.TENBAC) for bac in CAPBAC.objects.all()]
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})
        # Lấy danh sách MANGACH từ NGACH
        self.fields['MANGACH'].choices = [(ngach.MANGACH, ngach.TENNGACH) for ngach in NGACH.objects.all()]
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})
        
    def clean_GIOITINH(self):
        gioi_tinh = self.cleaned_data.get('GIOITINH')
        return True if gioi_tinh == 'Nam' else False