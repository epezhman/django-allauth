# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import allauth.socialaccount.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('provider', models.CharField(verbose_name='provider', choices=[('linkedin_oauth2', 'LinkedIn'), ('xing', 'Xing'), ('github', 'GitHub')], max_length=30)),
                ('uid', models.CharField(verbose_name='uid', max_length=255)),
                ('last_login', models.DateTimeField(verbose_name='last login', auto_now=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', auto_now_add=True)),
                ('extra_data', allauth.socialaccount.fields.JSONField(default='{}', verbose_name='extra data')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'social account',
                'verbose_name_plural': 'social accounts',
            },
        ),
        migrations.CreateModel(
            name='SocialApp',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('provider', models.CharField(verbose_name='provider', choices=[('linkedin_oauth2', 'LinkedIn'), ('xing', 'Xing'), ('github', 'GitHub')], max_length=30)),
                ('name', models.CharField(verbose_name='name', max_length=40)),
                ('client_id', models.CharField(verbose_name='client id', max_length=100, help_text='App ID, or consumer key')),
                ('secret', models.CharField(verbose_name='secret key', max_length=100, help_text='API secret, client secret, or consumer secret')),
                ('key', models.CharField(verbose_name='key', max_length=100, blank=True, help_text='Key')),
                ('sites', models.ManyToManyField(to='sites.Site', blank=True)),
            ],
            options={
                'verbose_name': 'social application',
                'verbose_name_plural': 'social applications',
            },
        ),
        migrations.CreateModel(
            name='SocialToken',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('token', models.TextField(verbose_name='token', help_text='"oauth_token" (OAuth1) or access token (OAuth2)')),
                ('token_secret', models.TextField(verbose_name='token secret', blank=True, help_text='"oauth_token_secret" (OAuth1) or refresh token (OAuth2)')),
                ('expires_at', models.DateTimeField(null=True, verbose_name='expires at', blank=True)),
                ('account', models.ForeignKey(to='socialaccount.SocialAccount')),
                ('app', models.ForeignKey(to='socialaccount.SocialApp')),
            ],
            options={
                'verbose_name': 'social application token',
                'verbose_name_plural': 'social application tokens',
            },
        ),
        migrations.AlterUniqueTogether(
            name='socialtoken',
            unique_together=set([('app', 'account')]),
        ),
        migrations.AlterUniqueTogether(
            name='socialaccount',
            unique_together=set([('provider', 'uid')]),
        ),
    ]
