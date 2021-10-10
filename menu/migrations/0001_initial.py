# Generated by Django 3.2.7 on 2021-09-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.CharField(max_length=400)),
                ('price', models.FloatField(default=0)),
                ('vegetarian', models.BooleanField(default=False)),
            ],
        ),
    ]
