# Generated by Django 2.2.1 on 2020-02-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='111@qq.com', max_length=254),
        ),
    ]