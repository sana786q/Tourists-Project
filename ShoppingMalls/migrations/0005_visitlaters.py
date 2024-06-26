# Generated by Django 4.1.2 on 2023-04-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingMalls', '0004_shoppingmallreviewrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitLaterS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mall_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=250)),
                ('category', models.CharField(default='Shopping_Mall', max_length=50)),
            ],
            options={
                'verbose_name': 'VisitLaterS',
                'verbose_name_plural': 'Visit Later',
            },
        ),
    ]
