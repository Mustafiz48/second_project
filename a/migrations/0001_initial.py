# Generated by Django 2.0.5 on 2018-08-31 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import first_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ads_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(default=first_app.models.ads_post.number, unique=True)),
                ('title', models.CharField(max_length=264)),
                ('picture', models.ImageField(blank='True', upload_to='')),
                ('picture2', models.ImageField(blank='True', upload_to='')),
                ('picture3', models.ImageField(blank='True', upload_to='')),
                ('category', models.CharField(choices=[('Family', 'Family'), ('Bachelor Mess', 'Bachelor Mess'), ('Female Mess', 'Famale Mess'), ('Office', 'Office'), ('Others', 'Others')], default='Family', max_length=264)),
                ('bed', models.CharField(max_length=264)),
                ('bath', models.CharField(max_length=264)),
                ('kitchen', models.CharField(max_length=264)),
                ('area', models.CharField(max_length=264)),
                ('district', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Mymensingh', 'Mymensingh'), ('Sylhet', 'Sylhet'), ('Barishal', ' Barisal'), ('Chattagram', 'Chattagram'), ('Rangpur', 'Rangpur'), ('Jessore', 'Jessore'), ('Jamalpur', 'Jamalpur'), ('Tangail', 'Tangail'), ('Lakshmipur', 'Lakshmipur'), ('Shatkhira', 'Shatkhira'), ('Bagerhat', 'Bagerhat'), ('Kishorgonj', 'Kishorgonj')], default='Dhaka', max_length=264)),
                ('divission', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Mymensingh', 'Mymensingh'), ('Sylhet', 'Sylhet'), ('Barishal', ' Barisal'), ('Chattagram', 'Chattagram'), ('Rangpur', 'Rangpur')], default='Dhaka', max_length=264)),
                ('address', models.CharField(max_length=264)),
                ('description', models.CharField(max_length=264)),
                ('cost', models.IntegerField()),
                ('mobile', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarcker', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user_signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=264)),
                ('Mobile', models.CharField(max_length=11)),
                ('Address', models.CharField(max_length=264)),
                ('District', models.CharField(max_length=264)),
                ('Zip', models.CharField(max_length=264)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]