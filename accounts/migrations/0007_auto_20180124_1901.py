# Generated by Django 2.0.1 on 2018-01-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180124_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/avatar.png', null=True, upload_to='avatars/', verbose_name='avatar para tu perfil'),
        ),
    ]
