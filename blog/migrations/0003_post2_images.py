# Generated by Django 4.1.4 on 2023-05-16 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post2',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
