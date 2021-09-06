# Generated by Django 3.2.7 on 2021-09-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(),
        ),
    ]
