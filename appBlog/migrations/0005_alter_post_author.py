# Generated by Django 4.2.1 on 2023-07-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]