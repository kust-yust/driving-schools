# Generated by Django 3.2 on 2021-04-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='pruebas',
            options={'verbose_name': 'Prueba', 'verbose_name_plural': 'Pruebas'},
        ),
    ]
