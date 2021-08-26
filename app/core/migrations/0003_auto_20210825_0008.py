# Generated by Django 3.2.6 on 2021-08-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_predict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='neutral',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_change_one_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_change_one_hour',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_change_one_month',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_change_one_year',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_change_seven_days',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_change_since_ath',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_forecast_four',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_forecast_one',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_forecast_three',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_forecast_two',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_prediction_one_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_prediction_one_month',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='price_prediction_one_year',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='rank_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='rank_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='rank_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='rank_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predict',
            name='sell',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
