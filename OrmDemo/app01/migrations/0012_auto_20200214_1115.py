# Generated by Django 2.2.1 on 2020-02-14 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20200213_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'book'},
        ),
        migrations.AlterModelOptions(
            name='publish',
            options={'verbose_name_plural': 'publish'},
        ),
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app01.Publish'),
        ),
    ]
