# Generated by Django 2.2.4 on 2019-09-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photfolio',
            name='photimg',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='photfolio',
            name='popupimg',
            field=models.ImageField(upload_to='media'),
        ),
    ]
