# Generated by Django 2.2.5 on 2020-03-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0003_auto_20200214_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdata',
            name='credit_card',
            field=models.TextField(default=True, null=True),
        ),
    ]