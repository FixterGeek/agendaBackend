# Generated by Django 2.0.1 on 2018-01-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('expiry', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('starts', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.CharField(choices=[('Activo', 'Activo'), ('Cumplido', 'Cumplido'), ('Vencido', 'Vencido')], max_length=100)),
                ('priority', models.CharField(choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=100)),
            ],
        ),
    ]
