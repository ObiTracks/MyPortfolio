# Generated by Django 3.1.4 on 2021-01-16 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_introcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='introcontent',
            name='btn2link',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AddField(
            model_name='introcontent',
            name='btn3link',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='introcontent',
            name='btn1link',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='introcontent',
            name='email',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
    ]
