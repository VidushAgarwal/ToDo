# Generated by Django 4.0.4 on 2022-04-21 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='uname',
        ),
    ]
