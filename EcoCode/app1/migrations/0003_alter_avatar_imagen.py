# Generated by Django 4.0.3 on 2022-05-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_avatar_nuevos_delete_detalles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='avatares'),
        ),
    ]