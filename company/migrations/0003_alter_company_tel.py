# Generated by Django 3.2.8 on 2021-10-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='tel',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
