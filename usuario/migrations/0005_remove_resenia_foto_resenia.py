# Generated by Django 4.2.2 on 2023-07-15 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_resenia_foto_resenia_delete_fotoresenia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resenia',
            name='foto_resenia',
        ),
    ]
