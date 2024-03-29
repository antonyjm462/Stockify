# Generated by Django 2.0.2 on 2019-08-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Change',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='High',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='LastTradedPrice',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Low',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Open',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='PercentChange',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='PercentChange30',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='PercentChange365',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='TradedValInCrs',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='TradedVolInLacs',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='WeekHigh52',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='WeekLow52',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]
