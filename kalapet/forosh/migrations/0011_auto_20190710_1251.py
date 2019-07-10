# Generated by Django 2.2.2 on 2019-07-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forosh', '0010_auto_20190710_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('axprofile', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Vets',
        ),
    ]
