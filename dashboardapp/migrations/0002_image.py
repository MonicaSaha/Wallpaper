# Generated by Django 3.0.4 on 2020-03-29 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('url', models.URLField(default=' ', max_length=5000)),
                ('Image_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(default=' ', upload_to='image')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.Category')),
            ],
        ),
    ]
