# Generated by Django 3.1.7 on 2021-04-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210406_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='slowmode',
            field=models.BooleanField(default=False),
        ),
    ]
