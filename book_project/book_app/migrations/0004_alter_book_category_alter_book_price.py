# Generated by Django 5.0 on 2024-01-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Medical', 'Medical'), ('Science fiction', 'Science fiction'), ('PSC', 'PSC'), ('Polictics', 'Polictics'), ('Finance', 'Finance'), ('Fiction', 'Fiction'), ('Ohters', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
