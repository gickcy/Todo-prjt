# Generated by Django 4.2.4 on 2023-09-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-04-22'),
            preserve_default=False,
        ),
    ]
