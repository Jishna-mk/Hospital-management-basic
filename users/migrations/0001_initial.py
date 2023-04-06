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
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Vaccination_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Vaccinated_Date', models.CharField(blank=True, max_length=200, null=True)),
                ('Vaccination_Document', models.FileField(blank=True, max_length=200, null=True, upload_to='vaccines')),
                ('user_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Phone_Number', models.CharField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('Age', models.CharField(blank=True, max_length=200, null=True)),
                ('User_photo', models.ImageField(blank=True, null=True, upload_to='users')),
                ('user_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_ID', models.IntegerField(blank=True, null=True)),
                ('Doctor_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Patient_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Booking_Date', models.DateField(blank=True, max_length=200, null=True)),
                ('Booking_Time', models.CharField(blank=True, max_length=200, null=True)),
                ('Reason', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('Doctor_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
