# Generated by Django 3.1.6 on 2021-02-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default='NO IMAGE', upload_to='images'),
        ),
    ]
