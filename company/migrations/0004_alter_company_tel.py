# Generated by Django 3.2.8 on 2021-10-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='tel',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
