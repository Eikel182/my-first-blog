# Generated by Django 2.1.7 on 2019-06-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outils', '0010_result_printer_mate'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='pattern_proto_cost_label',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='pattern_proto_mate_label',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]