# Generated by Django 4.1.5 on 2023-02-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='brief',
            field=models.CharField(max_length=100),
        ),
    ]
