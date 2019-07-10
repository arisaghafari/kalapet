# Generated by Django 2.2.2 on 2019-07-10 07:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forosh', '0007_auto_20190708_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='advertisment',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('سگ', 'سگ'), ('گربه', 'گربه'), ('ماهی', 'ماهی'), ('پرنده', 'پرنده'), ('جونده', 'جونده'), ('خزنده', 'خزنده')], max_length=200),
        ),
    ]
