# Generated by Django 3.2.5 on 2021-07-31 11:01

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('expired',)},
        ),
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
