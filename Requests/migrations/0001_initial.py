# Generated by Django 2.2.5 on 2020-02-14 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Students', '0001_initial'),
        ('Program', '0004_auto_20200127_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('year_of_graduation', models.CharField(max_length=5)),
                ('name_in_ar', models.CharField(max_length=100)),
                ('name_in_en', models.CharField(max_length=100)),
                ('cert_type', models.CharField(max_length=25)),
                ('degree', models.CharField(max_length=25)),
                ('copies_of_ar', models.IntegerField()),
                ('copies_of_en', models.IntegerField()),
                ('isAccepted', models.BooleanField(default=None)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Program.Program')),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.Student')),
            ],
        ),
    ]