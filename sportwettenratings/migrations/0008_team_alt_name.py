# Generated by Django 2.2.5 on 2022-03-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportwettenratings', '0007_auto_20220327_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='alt_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
