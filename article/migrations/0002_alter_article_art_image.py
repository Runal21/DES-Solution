# Generated by Django 5.0.4 on 2024-04-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_image',
            field=models.ImageField(upload_to='static/article/article_images'),
        ),
    ]