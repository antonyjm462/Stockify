# Generated by Django 2.0.2 on 2019-08-28 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190828_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
