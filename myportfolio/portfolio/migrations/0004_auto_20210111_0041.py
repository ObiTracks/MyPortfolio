# Generated by Django 3.1.4 on 2021-01-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210110_2203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='image',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='media/', verbose_name='Image'),
        ),
    ]
