# Generated by Django 5.1.3 on 2024-12-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_profilis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilis',
            name='nuotrauka',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]