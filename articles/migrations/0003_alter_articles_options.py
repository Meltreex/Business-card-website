# Generated by Django 5.0.7 on 2024-07-11 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articles_options_alter_articles_intro_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статиь'},
        ),
    ]
