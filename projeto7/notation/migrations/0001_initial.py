# Generated by Django 4.1.1 on 2022-09-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb_works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('subtitle', models.CharField(max_length=80)),
                ('work', models.TextField()),
            ],
        ),
    ]