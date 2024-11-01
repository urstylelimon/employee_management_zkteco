# Generated by Django 4.2.4 on 2024-10-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='house_number',
            field=models.CharField(default='N/A', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='road_number',
            field=models.CharField(choices=[('Road 1', 'Road 1'), ('Road 2', 'Road 2'), ('Road 3', 'Road 3'), ('Road 4', 'Road 4'), ('Road 5', 'Road 5'), ('Road 6', 'Road 6'), ('Road 7', 'Road 7'), ('Road 8', 'Road 8'), ('Road 9', 'Road 9'), ('Road 10', 'Road 10'), ('Road 11', 'Road 11'), ('Road 12', 'Road 12'), ('Road 13', 'Road 13'), ('Road 14', 'Road 14'), ('UN Road', 'UN Road'), ('Park Road', 'Park Road')], default='Road 1', max_length=10),
            preserve_default=False,
        ),
    ]
