# Generated by Django 4.1.5 on 2023-02-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_book_brief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link_photo',
            field=models.CharField(max_length=255),
        ),
    ]
