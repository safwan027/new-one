# Generated by Django 5.0 on 2023-12-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book_category_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
