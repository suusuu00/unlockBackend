# Generated by Django 4.2.1 on 2023-06-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlock2023', '0002_alter_reservation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(choices=[('09:00', '1'), ('10:00', '2'), ('11:00', '3'), ('12:00', '4'), ('13:00', '5'), ('14:00', '6'), ('15:00', '7'), ('16:00', '8'), ('17:00', '9'), ('18:00', '10')], max_length=10),
        ),
    ]
