# Generated by Django 4.2.3 on 2023-08-21 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0001_initial'),
        ('question', '0002_alter_question_qty_responses'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='division.division'),
            preserve_default=False,
        ),
    ]
