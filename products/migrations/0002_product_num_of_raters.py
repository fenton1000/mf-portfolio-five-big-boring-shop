# Generated by Django 3.2 on 2023-04-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_of_raters',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]