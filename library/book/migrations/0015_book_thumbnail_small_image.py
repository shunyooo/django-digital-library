# Generated by Django 2.2 on 2019-04-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_auto_20190406_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail_small_image',
            field=models.ImageField(max_length=500, null=True, upload_to=''),
        ),
    ]
