# Generated by Django 3.1.7 on 2021-04-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='code',
            field=models.CharField(default='309609', max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(max_length=400),
        ),
    ]
