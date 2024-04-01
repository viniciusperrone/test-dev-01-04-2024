# Generated by Django 4.0.3 on 2024-04-01 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_consumer_discount_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='discount_rule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount_rule', to='calculator.discountrules', verbose_name='Desconto'),
        ),
    ]
