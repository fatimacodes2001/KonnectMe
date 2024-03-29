# Generated by Django 3.1.4 on 2021-01-18 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'get_latest_by': 'job_id'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'get_latest_by': 'update_id'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'get_latest_by': 'update_id'},
        ),
        migrations.RenameField(
            model_name='photos',
            old_name='num_lhares',
            new_name='num_shares',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='location',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_col',
        ),
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='location',
        ),
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='state',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='photos',
            name='city',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='photos',
            name='state',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='profilesharesphotos',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profilesharesstatus',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='state',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='pagelikesstatus',
            name='update',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.status'),
        ),
    ]
