# Generated by Django 3.1.7 on 2021-03-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210314_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='toys',
            field=models.ManyToManyField(blank=True, to='main_app.Toy'),
        ),
    ]
