# Generated by Django 4.1.2 on 2023-04-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itblog', '0005_alter_article_created_on_alter_article_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructions',
            name='objective',
            field=models.CharField(max_length=100),
        ),
    ]