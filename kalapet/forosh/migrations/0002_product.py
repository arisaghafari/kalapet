# Generated by Django 2.2.2 on 2019-06-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forosh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('description', models.TextField()),
                ('supplier', models.CharField(max_length=200)),
                ('expiration', models.DateField()),
            ],
        ),
    ]
