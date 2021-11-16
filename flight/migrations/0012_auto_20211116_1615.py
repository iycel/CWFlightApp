# Generated by Django 3.2.9 on 2021-11-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0011_auto_20211116_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passenger',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(choices=[('004', 'Tokyo'), ('61', 'Trabzon'), ('005', 'Sidney'), ('06', 'Ankara'), ('34', 'Istanbul'), ('07', 'Antalya'), ('002', 'London'), ('001', 'Berlin'), ('003', 'New York'), ('35', 'Izmir')], max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(choices=[('004', 'Tokyo'), ('61', 'Trabzon'), ('005', 'Sidney'), ('06', 'Ankara'), ('34', 'Istanbul'), ('07', 'Antalya'), ('002', 'London'), ('001', 'Berlin'), ('003', 'New York'), ('35', 'Izmir')], max_length=50),
        ),
        migrations.AlterField(
            model_name='operatingairlines',
            name='name',
            field=models.CharField(choices=[('905', 'Atlasglobal'), ('903', 'Turkish Airlines'), ('902', 'Anadolu Jet'), ('904', 'Pegasus'), ('901', 'Onur Air')], max_length=50),
        ),
    ]