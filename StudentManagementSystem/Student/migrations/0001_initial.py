# Generated by Django 4.2.3 on 2023-07-28 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=30)),
                ('Reg_no', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=50)),
                ('Taluka', models.CharField(max_length=30)),
                ('District', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='media/img')),
                ('pincode', models.CharField(max_length=30)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=30)),
                ('marks', models.CharField(max_length=30)),
                ('Semester', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('Registration_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student_details')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=30)),
                ('feedback', models.TextField(max_length=1000)),
                ('Registration_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.marks')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admission_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_name', models.CharField(max_length=30)),
                ('Class_name', models.CharField(max_length=30)),
                ('Branch', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('Date_of_Admission', models.DateField()),
                ('Semester', models.CharField(max_length=30)),
                ('registration_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student_details')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
