# Generated by Django 3.2.8 on 2021-11-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_auto_20211114_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(choices=[('004', 'Tokyo'), ('005', 'Sidney'), ('001', 'Berlin'), ('07', 'Antalya'), ('06', 'Ankara'), ('61', 'Trabzon'), ('34', 'Istanbul'), ('003', 'New York'), ('002', 'London'), ('35', 'Izmir')], max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(choices=[('004', 'Tokyo'), ('005', 'Sidney'), ('001', 'Berlin'), ('07', 'Antalya'), ('06', 'Ankara'), ('61', 'Trabzon'), ('34', 'Istanbul'), ('003', 'New York'), ('002', 'London'), ('35', 'Izmir')], max_length=50),
        ),
        migrations.AlterField(
            model_name='operatingairlines',
            name='name',
            field=models.CharField(choices=[('903', 'Turkish Airlines'), ('904', 'Pegasus'), ('901', 'Onur Air'), ('905', 'Atlasglobal'), ('902', 'Anadolu Jet')], max_length=50),
        ),
    ]