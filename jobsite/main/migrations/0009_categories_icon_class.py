# Generated by Django 4.1.7 on 2023-04-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_job_postings_howtoapply'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='icon_class',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
