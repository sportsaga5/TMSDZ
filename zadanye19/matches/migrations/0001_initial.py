# Generated by Django 4.0.6 on 2022-07-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team', models.CharField(max_length=50)),
                ('second_team', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('stadium', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
            ],
        ),
    ]