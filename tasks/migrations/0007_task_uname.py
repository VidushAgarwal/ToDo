# Generated by Django 4.0.4 on 2022-04-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_task_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='uname',
            field=models.CharField(default='Vidush', max_length=100),
        ),
    ]