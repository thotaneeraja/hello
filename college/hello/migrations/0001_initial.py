# Generated by Django 4.0 on 2021-12-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='next',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=10)),
                ('phonenumber', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
