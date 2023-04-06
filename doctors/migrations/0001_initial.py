# Generated by Django 4.1.5 on 2023-03-16 09:56

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
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Specialised_In', models.CharField(blank=True, max_length=200, null=True)),
                ('Experience', models.TextField(blank=True, max_length=200, null=True)),
                ('Clinic_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Contact_Number', models.CharField(blank=True, max_length=200, null=True)),
                ('Clinic_Address', models.TextField(blank=True, max_length=200, null=True)),
                ('About', models.TextField(blank=True, max_length=200, null=True)),
                ('Doctor_Photo', models.ImageField(blank=True, null=True, upload_to='doctors')),
                ('doctor_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
