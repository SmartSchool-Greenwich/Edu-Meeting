# Generated by Django 4.2.7 on 2024-03-07 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_academicyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicyear',
            name='faculties',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='home.faculties'),
            preserve_default=False,
        ),
    ]