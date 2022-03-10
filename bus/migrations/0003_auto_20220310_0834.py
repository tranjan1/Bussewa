# Generated by Django 3.1.6 on 2022-03-10 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_alter_bus_seat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat_type',
            field=models.CharField(choices=[('3*3', '3*3'), ('3*2', '3*2'), ('1*2', '1*2'), ('2*3', '2*3'), ('2*1', '2*1'), ('2*2', '2*2'), ('1*1', '1*1')], max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='paymentintent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pickuppoint',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='services',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
