# Generated by Django 3.2.7 on 2021-09-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0005_auto_20210930_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('2*2', '2*2'), ('1*2', '1*2'), ('2*1', '2*1'), ('2*3', '2*3'), ('3*3', '3*3'), ('3*2', '3*2'), ('1*1', '1*1')], max_length=100),
        ),
    ]