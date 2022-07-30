# Generated by Django 4.0.6 on 2022-07-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='images')),
                ('end_of_certificate', models.DateField(default=0)),
                ('end_of_drivers_license', models.DateField(default=0)),
                ('end_of_hygiene_license', models.DateField(default=0)),
                ('end_of_smart_license', models.DateField(default=0)),
            ],
        ),
    ]