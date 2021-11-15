# Generated by Django 3.2.8 on 2021-11-14 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flight', '0003_auto_20211114_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(choices=[('07', 'Antalya'), ('06', 'Ankara'), ('001', 'Berlin'), ('002', 'London'), ('34', 'Istanbul'), ('35', 'Izmir'), ('005', 'Sidney'), ('61', 'Trabzon'), ('004', 'Tokyo'), ('003', 'New York')], default='06', max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.city'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='operating_airlines',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.operatingairlines'),
        ),
        migrations.AlterField(
            model_name='flightreservation',
            name='first_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flightreservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flight.flight'),
        ),
        migrations.AlterField(
            model_name='operatingairlines',
            name='name',
            field=models.CharField(choices=[('904', 'Pegasus'), ('905', 'Atlasglobal'), ('903', 'Turkish Airlines'), ('902', 'Anadolu Jet'), ('901', 'Onur Air')], default='06', max_length=50, verbose_name='Airlines'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight'),
        ),
    ]