# Generated by Django 3.1.4 on 2021-01-12 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_col', models.CharField(blank=True, max_length=45, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('num_photos', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('businessid', models.IntegerField(blank=True, db_column='businessId', null=True)),
                ('companytype', models.CharField(blank=True, db_column='companyType', max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('aboutyou', models.CharField(blank=True, db_column='aboutYou', max_length=1000, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('state', models.CharField(blank=True, max_length=45, null=True)),
                ('numfollowers', models.IntegerField(blank=True, db_column='numFollowers', null=True)),
            ],
            options={
                'db_table': 'page',
            },
        ),
        migrations.CreateModel(
            name='RegularProfile',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=45, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('about_you', models.CharField(blank=True, max_length=1000, null=True)),
                ('work_profile', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('state', models.CharField(blank=True, max_length=45, null=True)),
                ('p_grad', models.CharField(blank=True, max_length=250, null=True)),
                ('u_grad', models.CharField(blank=True, max_length=250, null=True)),
                ('high_school', models.CharField(blank=True, max_length=250, null=True)),
                ('further_education', models.CharField(blank=True, db_column='Further_education', max_length=250, null=True)),
                ('num_followers', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'regular_profile',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_id', models.IntegerField()),
                ('caption', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('num_shares', models.IntegerField(blank=True, null=True)),
                ('num_likes', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=45, null=True)),
                ('page_email', models.ForeignKey(blank=True, db_column='page_email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.page')),
                ('regular_profile_email', models.ForeignKey(blank=True, db_column='regular_profile_email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_id', models.IntegerField()),
                ('caption', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('num_likes', models.IntegerField(blank=True, null=True)),
                ('num_lhares', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.album')),
                ('page_email', models.ForeignKey(blank=True, db_column='page_email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.page')),
                ('regular_profile_email', models.ForeignKey(blank=True, db_column='regular_profile_email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'photos',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('num_posts', models.IntegerField(blank=True, null=True)),
                ('num_hours', models.IntegerField(blank=True, null=True)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_detail', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('postdate', models.DateTimeField(blank=True, null=True)),
                ('page_email', models.ForeignKey(db_column='page_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.page')),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='page_email',
            field=models.ForeignKey(blank=True, db_column='page_email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.page'),
        ),
        migrations.AddField(
            model_name='album',
            name='regular_profile_email',
            field=models.ForeignKey(blank=True, db_column='regular_profile_email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile'),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.regularprofile')),
                ('skill', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'skills',
                'unique_together': {('email', 'skill')},
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.regularprofile')),
                ('interest', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'interests',
                'unique_together': {('email', 'interest')},
            },
        ),
        migrations.CreateModel(
            name='ProfileSharesStatus',
            fields=[
                ('update', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.status')),
                ('share_id', models.IntegerField()),
                ('regular_profile_email', models.ForeignKey(db_column='regular_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'profile_shares_status',
                'unique_together': {('update', 'regular_profile_email', 'share_id')},
            },
        ),
        migrations.CreateModel(
            name='ProfileSharesPhotos',
            fields=[
                ('update', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.photos')),
                ('share_id', models.IntegerField()),
                ('regular_profile_email', models.ForeignKey(db_column='regular_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'profile_shares_photos',
                'unique_together': {('update', 'regular_profile_email', 'share_id')},
            },
        ),
        migrations.CreateModel(
            name='ProfileLikesStatus',
            fields=[
                ('update', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.status')),
                ('status_like_id', models.IntegerField()),
                ('regular_profile_email', models.ForeignKey(db_column='regular_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'profile_likes_status',
                'unique_together': {('update', 'regular_profile_email', 'status_like_id')},
            },
        ),
        migrations.CreateModel(
            name='ProfileLikesPhotos',
            fields=[
                ('update', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.photos')),
                ('photo_like_id', models.IntegerField()),
                ('regular_profile_email', models.ForeignKey(db_column='regular_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'profile_likes_photos',
                'unique_together': {('update', 'regular_profile_email', 'photo_like_id')},
            },
        ),
        migrations.CreateModel(
            name='ProfileFollowsProfile',
            fields=[
                ('follower_email', models.OneToOneField(db_column='follower_email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.regularprofile')),
                ('followed_profile_email', models.ForeignKey(db_column='followed_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='application.regularprofile')),
            ],
            options={
                'db_table': 'profile_follows_profile',
                'unique_together': {('follower_email', 'followed_profile_email')},
            },
        ),
        migrations.CreateModel(
            name='ProfileFollowsPage',
            fields=[
                ('page_email', models.OneToOneField(db_column='page_email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.page')),
                ('regular_profile_email', models.ForeignKey(db_column='regular_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'profile_follows_page',
                'unique_together': {('page_email', 'regular_profile_email')},
            },
        ),
        migrations.CreateModel(
            name='PageLikesStatus',
            fields=[
                ('update', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.photos')),
                ('status_like_id', models.IntegerField()),
                ('page_email', models.ForeignKey(db_column='page_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.page')),
            ],
            options={
                'db_table': 'page_likes_status',
                'unique_together': {('update', 'page_email', 'status_like_id')},
            },
        ),
        migrations.CreateModel(
            name='PageLikesPhotos',
            fields=[
                ('update', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.photos')),
                ('photo_like_id', models.IntegerField()),
                ('page_email', models.ForeignKey(db_column='page_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.page')),
            ],
            options={
                'db_table': 'page_likes_photos',
                'unique_together': {('update', 'page_email', 'photo_like_id')},
            },
        ),
        migrations.CreateModel(
            name='PageFollowsProfile',
            fields=[
                ('follower_page_email', models.OneToOneField(db_column='follower_page_email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.page')),
                ('followed_profile_email', models.ForeignKey(db_column='followed_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'page_follows_profile',
                'unique_together': {('follower_page_email', 'followed_profile_email')},
            },
        ),
        migrations.CreateModel(
            name='PageFollowsPage',
            fields=[
                ('follower_email', models.OneToOneField(db_column='follower_email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.page')),
                ('followed_page_email', models.ForeignKey(db_column='followed_page_email', on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='application.page')),
            ],
            options={
                'db_table': 'page_follows_page',
                'unique_together': {('follower_email', 'followed_page_email')},
            },
        ),
        migrations.CreateModel(
            name='AppliesFor',
            fields=[
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='application.job')),
                ('regular_profile_email', models.ForeignKey(db_column='regular_profile_email', on_delete=django.db.models.deletion.DO_NOTHING, to='application.regularprofile')),
            ],
            options={
                'db_table': 'applies_for',
                'unique_together': {('job', 'regular_profile_email')},
            },
        ),
    ]
