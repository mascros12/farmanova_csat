# Generated by Django 4.2.3 on 2023-08-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0001_initial'),
        ('form', '0002_form_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='division',
            field=models.ManyToManyField(blank=True, to='division.division'),
        ),
    ]
