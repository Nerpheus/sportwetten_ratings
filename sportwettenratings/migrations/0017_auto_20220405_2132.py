# Generated by Django 2.2.5 on 2022-04-05 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportwettenratings', '0016_auto_20220403_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='free_kicks_a',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='free_kicks_h',
            field=models.IntegerField(null=True),
        ),
    ]
