# Generated by Django 4.2.2 on 2023-07-14 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_resenia_fotoresenia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotoresenia',
            old_name='avatar',
            new_name='foto_resenia',
        ),
    ]
