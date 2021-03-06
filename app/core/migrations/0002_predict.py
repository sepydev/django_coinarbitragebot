# Generated by Django 3.2.6 on 2021-08-24 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price_change_one_hour', models.FloatField(blank=True)),
                ('price_change_one_day', models.FloatField(blank=True)),
                ('price_change_seven_days', models.FloatField(blank=True)),
                ('price_change_one_month', models.FloatField(blank=True)),
                ('price_change_one_year', models.FloatField(blank=True)),
                ('price_change_since_ath', models.FloatField(blank=True)),
                ('price_prediction_one_day', models.FloatField(blank=True)),
                ('price_prediction_one_month', models.FloatField(blank=True)),
                ('price_prediction_one_year', models.FloatField(blank=True)),
                ('price_forecast_one', models.FloatField(blank=True)),
                ('price_forecast_two', models.FloatField(blank=True)),
                ('price_forecast_three', models.FloatField(blank=True)),
                ('price_forecast_four', models.FloatField(blank=True)),
                ('sell', models.IntegerField(blank=True)),
                ('neutral', models.IntegerField(blank=True)),
                ('buy', models.IntegerField(blank=True)),
                ('rank_1', models.IntegerField(blank=True)),
                ('rank_2', models.IntegerField(blank=True)),
                ('rank_3', models.IntegerField(blank=True)),
                ('rank_4', models.IntegerField(blank=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.coin')),
            ],
        ),
    ]
