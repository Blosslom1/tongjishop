# Generated by Django 3.2.12 on 2022-03-15 03:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='user_portrait',
            field=models.ImageField(default='1.png', upload_to='', verbose_name='头像'),
        ),
        migrations.CreateModel(
            name='AmountMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='金额')),
                ('consume', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='开销')),
                ('integral', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='积分')),
                ('integral_consume', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(22)], verbose_name='积分开销')),
                ('user_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_page.userdata')),
            ],
            options={
                'verbose_name_plural': '用户金额/积分',
                'db_table': 'amount_money',
            },
        ),
    ]
