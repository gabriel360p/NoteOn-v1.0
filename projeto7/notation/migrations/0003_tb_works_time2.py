# Generated by Django 4.1.1 on 2022-09-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notation', '0002_tb_works_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_works',
            name='time2',
            field=models.DateTimeField(auto_now=True),
        ),
    ]