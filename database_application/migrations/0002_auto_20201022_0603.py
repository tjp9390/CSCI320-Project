# Generated by Django 3.0.7 on 2020-10-22 06:03

import django.contrib.postgres.fields
#import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
#from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):

    dependencies = [
        ('database_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('IngredientName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('AmountLeft', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Makes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DatesMade', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('RecipeName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('PreparationTime', models.PositiveIntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ServingSize', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('LocationID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('LocationType', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Utensil',
            fields=[
                ('UtensilName', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='u_name',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='u_uid',
        ),
        migrations.AddField(
            model_name='user',
            name='UID',
            field=models.PositiveIntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('StepNumber', models.PositiveIntegerField(primary_key=True, serialize=False)),
                #('QuantitiesOfIngredients', django.contrib.postgres.fields.hstore.HStoreField()),
                ('Instructions', models.TextField(max_length=400)),
                ('Ingredients', models.ManyToManyField(to='database_application.Ingredient')),
                ('RecipeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_application.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='Users',
            field=models.ManyToManyField(through='database_application.Makes', to='database_application.User'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='Utensils',
            field=models.ManyToManyField(to='database_application.Utensil'),
        ),
        migrations.AddField(
            model_name='makes',
            name='Recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_application.Recipe'),
        ),
        migrations.AddField(
            model_name='makes',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_application.User'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='StorageLocations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_application.StorageLocation'),
        ),
        migrations.AddField(
            model_name='user',
            name='StorageLocations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database_application.StorageLocation'),
        ),
    ]