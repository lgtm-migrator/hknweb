# Generated by Django 2.2.8 on 2021-10-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hknweb', '0014_auto_20210202_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text="Formats: '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y' (Examples: '2006-10-25', '10/25/2006', '10/25/06')", null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='graduation_date',
            field=models.DateField(blank=True, help_text="Formats: '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y' (Examples: '2006-10-25', '10/25/2006', '10/25/06')", null=True),
        ),
    ]
