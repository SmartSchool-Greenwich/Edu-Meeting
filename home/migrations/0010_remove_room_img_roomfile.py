# Generated by Django 5.0.3 on 2024-04-01 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_pageview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='img',
        ),
        migrations.CreateModel(
            name='RoomFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='room_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='home.room')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile')),
            ],
        ),
    ]
