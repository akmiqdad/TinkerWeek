# Generated by Django 3.1.4 on 2021-01-10 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210106_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='participent',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='website.event'),
        ),
    ]