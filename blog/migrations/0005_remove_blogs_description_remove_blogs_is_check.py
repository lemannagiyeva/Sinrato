# Generated by Django 5.1.1 on 2024-10-05 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_blod_types_blogs_blog_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='is_check',
        ),
    ]
