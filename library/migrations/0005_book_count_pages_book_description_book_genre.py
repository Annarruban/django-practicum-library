# Generated by Django 5.2 on 2025-04-03 11:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_publisher_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count_pages',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)]),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Science Fiction', 'Science Fiction'), ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Biography', 'Biography')], default='Non-Fiction', max_length=50),
        ),
    ]
