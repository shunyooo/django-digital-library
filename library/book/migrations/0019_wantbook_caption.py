# Generated by Django 2.2 on 2019-04-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_wantbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='wantbook',
            name='caption',
            field=models.TextField(null=True),
        ),
    ]
