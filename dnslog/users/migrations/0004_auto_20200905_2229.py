# Generated by Django 3.1.1 on 2020-09-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200905_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subdomain',
            field=models.CharField(db_index=True, max_length=128),
        ),
    ]
