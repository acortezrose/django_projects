# Generated by Django 2.1.5 on 2019-03-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0007_auto_20190321_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='justification',
            field=models.TextField(),
        ),
    ]