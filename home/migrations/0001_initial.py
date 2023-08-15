# Generated by Django 4.2.4 on 2023-08-14 04:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre de la marca (Michael Kors, Zara, Oscar de la Renta, Forever 21, etc.)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_creation', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_garment', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Ingrese una breve descripción de la prenda de ropa', max_length=1000)),
                ('size', models.CharField(max_length=5, verbose_name='SIZE')),
                ('brand', models.ManyToManyField(help_text='Seleccione una marca para este producto', to='home.brand')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.department')),
            ],
        ),
        migrations.CreateModel(
            name='GarmentInstance',
            fields=[
                ('id_garment', models.UUIDField(default=uuid.uuid4, help_text='ID único para cada prenda de ropa en particular en toda la biblioteca', primary_key=True, serialize=False)),
                ('dealer', models.CharField(max_length=200)),
                ('date_stock', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('u', 'Unstock'), ('o', 'On Shipping'), ('a', 'Available'), ('r', 'Reserved')], default='u', help_text='Disponibilidad de la prenda', max_length=1)),
                ('garment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.garment')),
            ],
            options={
                'ordering': ['date_stock'],
            },
        ),
    ]