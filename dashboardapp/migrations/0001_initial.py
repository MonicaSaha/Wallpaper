# Generated by Django 3.0.4 on 2020-03-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Category_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=1000)),
            ],
        ),
    ]
