# Generated by Django 4.0.3 on 2022-03-13 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Womt',
            fields=[
                ('work_order_name', models.SlugField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default='unknown', max_length=50)),
                ('status', models.CharField(choices=[('received', 'RECEIVED'), ('assigned', 'ASSIGNED'), ('additional dq work', 'ADDITIONAL DQ WORK'), ('closed', 'CLOSED')], default='new', max_length=50)),
                ('assigned_to', models.CharField(choices=[('dq', 'DQ'), ('care', 'CARE'), ('supply chain', 'SUPPLY CHAIN'), ('service', 'SERVICE'), ('m and a', 'M AND A')], default='DQ', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalWomt',
            fields=[
                ('work_order_name', models.SlugField(max_length=20)),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('created_by', models.CharField(default='unknown', max_length=50)),
                ('status', models.CharField(choices=[('received', 'RECEIVED'), ('assigned', 'ASSIGNED'), ('additional dq work', 'ADDITIONAL DQ WORK'), ('closed', 'CLOSED')], default='new', max_length=50)),
                ('assigned_to', models.CharField(choices=[('dq', 'DQ'), ('care', 'CARE'), ('supply chain', 'SUPPLY CHAIN'), ('service', 'SERVICE'), ('m and a', 'M AND A')], default='DQ', max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical womt',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
