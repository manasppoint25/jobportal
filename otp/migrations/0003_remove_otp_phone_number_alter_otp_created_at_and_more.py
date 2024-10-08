# Generated by Django 5.0.6 on 2024-10-07 09:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0002_otp_phone_number_alter_otp_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='otp',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]