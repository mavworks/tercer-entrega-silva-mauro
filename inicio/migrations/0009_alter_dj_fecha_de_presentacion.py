# Generated by Django 4.2.2 on 2023-08-08 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_dj_imagen_dj_invitado_imagen_invitado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dj',
            name='fecha_de_presentacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
