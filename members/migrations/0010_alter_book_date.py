# Generated by Django 4.1.5 on 2023-02-05 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_book_category_book_date_book_number_of_pages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
