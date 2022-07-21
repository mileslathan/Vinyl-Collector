# Generated by Django 4.0.6 on 2022-07-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('released', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
