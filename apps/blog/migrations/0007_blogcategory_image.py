# Generated by Django 4.1.3 on 2022-12-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]
