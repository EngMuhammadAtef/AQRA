# Generated by Django 4.1.5 on 2023-02-02 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
                ('email', models.CharField(max_length=101)),
                ('password1', models.CharField(max_length=22)),
            ],
        ),
    ]
