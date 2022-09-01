# Generated by Django 4.1 on 2022-09-01 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_measurment_measurement'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
