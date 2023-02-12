# Generated by Django 4.1.4 on 2023-02-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='about/')),
                ('from_address', models.CharField(max_length=100)),
                ('lives_in', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Edeucation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('last', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('last', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('percentage', models.IntegerField()),
                ('type', models.CharField(choices=[('Coding', 'Coding'), ('Design', 'Design')], max_length=10)),
            ],
        ),
    ]
