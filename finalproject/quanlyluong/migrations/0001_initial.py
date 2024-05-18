# Generated by Django 5.0.3 on 2024-05-18 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CAPBAC',
            fields=[
                ('MABAC', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('TENBAC', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GIANGVIEN',
            fields=[
                ('MAGIANGVIEN', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('HOTEN', models.CharField(max_length=50)),
                ('NGAYSINH', models.CharField(max_length=10)),
                ('GIOITINH', models.BooleanField()),
                ('SODIENTHOAI', models.CharField(max_length=10)),
                ('DIACHI', models.CharField(max_length=100)),
                ('NGAYVAOLAM', models.CharField(max_length=10)),
                ('CHUCVU', models.CharField(max_length=50)),
                ('SOTIETDAY', models.IntegerField()),
                ('MABAC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quanlyluong.capbac')),
            ],
        ),
        migrations.CreateModel(
            name='NGACH',
            fields=[
                ('MANGACH', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('TENNGACH', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TRINHDO',
            fields=[
                ('MATD', models.IntegerField(primary_key=True, serialize=False)),
                ('TENTD', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TAIKHOAN',
            fields=[
                ('giang_vien', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='quanlyluong.giangvien')),
                ('MATKHAU', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='giangvien',
            name='MANGACH',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quanlyluong.ngach'),
        ),
        migrations.AddField(
            model_name='giangvien',
            name='MATD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quanlyluong.trinhdo'),
        ),
        migrations.CreateModel(
            name='HESOLUONG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HESO', models.FloatField()),
                ('MABAC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quanlyluong.capbac')),
                ('MANGACH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quanlyluong.ngach')),
            ],
            options={
                'verbose_name_plural': 'Hệ số lương',
                'unique_together': {('MABAC', 'MANGACH')},
            },
        ),
    ]
