# Generated by Django 4.0.6 on 2022-07-24 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tenure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenure', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='plan',
            name='planID',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='promotion',
        ),
        migrations.AddField(
            model_name='plan',
            name='isPromotionActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plan',
            name='promotionCountByUser',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='promotionEndDate',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='plan',
            name='promotionStartDate',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='plan',
            name='promotionType',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.RemoveField(
            model_name='plan',
            name='amountOptions',
        ),
        migrations.AlterField(
            model_name='plan',
            name='benefitPercentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='benefitType',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plan',
            name='planName',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='plan',
            name='tenureOptions',
        ),
        migrations.AddField(
            model_name='plan',
            name='amountOptions',
            field=models.ManyToManyField(to='plan.amount'),
        ),
        migrations.AddField(
            model_name='plan',
            name='tenureOptions',
            field=models.ManyToManyField(to='plan.tenure'),
        ),
    ]
