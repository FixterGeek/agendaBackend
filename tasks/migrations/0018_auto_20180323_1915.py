# Generated by Django 2.0.1 on 2018-03-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20180323_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('Q3', 'Q3'), ('Q2', 'Q2'), ('Q1', 'Q1')], max_length=100),
        ),
    ]