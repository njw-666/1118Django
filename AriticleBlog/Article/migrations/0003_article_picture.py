# Generated by Django 2.2.1 on 2020-02-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_auto_20200217_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(default='01.jpg', upload_to='images', verbose_name='图片'),
            preserve_default=False,
        ),
    ]
