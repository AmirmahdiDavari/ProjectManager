# Generated by Django 3.2.10 on 2022-01-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddUser', '0003_auto_20220107_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='image',
            field=models.ImageField(null=True, upload_to='project/images', verbose_name='عکس'),
        ),
    ]