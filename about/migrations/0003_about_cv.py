# Generated by Django 4.1.4 on 2023-02-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='cv',
            field=models.FileField(default='', upload_to='about'),
            preserve_default=False,
        ),
    ]