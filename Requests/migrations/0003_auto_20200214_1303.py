# Generated by Django 2.2.5 on 2020-02-14 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0002_auto_20200214_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestdata',
            options={'base_manager_name': 'objects'},
        ),
    ]