# Generated by Django 3.1.2 on 2020-11-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0002_auto_20201121_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
