# Generated by Django 3.2.3 on 2021-05-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albamon',
            name='applicant',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='albamon',
            name='pay',
            field=models.IntegerField(default=8720),
        ),
    ]
