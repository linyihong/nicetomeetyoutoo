# Generated by Django 2.1.1 on 2018-09-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Detail',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='Time',
            field=models.DateTimeField(null=True),
        ),
    ]
