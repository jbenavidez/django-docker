# Generated by Django 3.2.9 on 2021-11-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyhistory',
            name='date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='companyhistory',
            name='img_url',
            field=models.TextField(),
        ),
    ]
