# Generated by Django 4.2.5 on 2023-09-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0012_alter_personal_cp_alter_personal_localidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='apellido_emergencia',
            field=models.CharField(default='a', max_length=60),
        ),
        migrations.AlterField(
            model_name='personal',
            name='nombre_emergencia',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='personal',
            name='numero_contacto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personal',
            name='vinculo',
            field=models.CharField(default='a', max_length=15),
        ),
    ]