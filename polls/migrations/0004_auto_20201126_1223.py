# Generated by Django 3.1.2 on 2020-11-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20201126_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]