# Generated by Django 2.2.1 on 2020-02-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='photo',
            field=models.ImageField(default='img/gtl.jpg', upload_to='img', verbose_name='图片'),
        ),
    ]
