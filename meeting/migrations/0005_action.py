# Generated by Django 2.0.1 on 2018-02-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_auto_20180227_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_action', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.BooleanField(default=False)),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='action', to='meeting.Meeting')),
            ],
        ),
    ]