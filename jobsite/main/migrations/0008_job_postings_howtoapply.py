# Generated by Django 4.1.7 on 2023-04-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_job_postings_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_postings',
            name='howtoapply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
