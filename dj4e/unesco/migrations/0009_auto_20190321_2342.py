# Generated by Django 2.1.5 on 2019-03-21 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0008_auto_20190321_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='site',
            name='justification',
            field=models.CharField(max_length=10000),
        ),
    ]
