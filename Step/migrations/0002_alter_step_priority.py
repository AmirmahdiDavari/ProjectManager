# Generated by Django 3.2.9 on 2021-12-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Step', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
