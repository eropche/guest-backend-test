# Generated by Django 2.2.3 on 2019-07-07 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghuest_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]
