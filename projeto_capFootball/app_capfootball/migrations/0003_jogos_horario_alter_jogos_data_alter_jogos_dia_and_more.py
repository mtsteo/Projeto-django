# Generated by Django 4.2 on 2023-04-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_capfootball', '0002_remove_jogos_jogoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogos',
            name='horario',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='data',
            field=models.DateField(default='null', max_length=15),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='dia',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='times',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
