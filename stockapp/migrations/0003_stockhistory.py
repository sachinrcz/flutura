# Generated by Django 2.1.2 on 2018-10-28 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0002_auto_20181028_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('low', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('high', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('close', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('volume', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='history', to='stockapp.Stock')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]