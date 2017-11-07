# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 14:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('addr', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '\u6821\u533a',
                'verbose_name_plural': '\u6821\u533a',
            },
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.SmallIntegerField(choices=[(0, b'\xe9\x9d\xa2\xe6\x8e\x88(\xe8\x84\xb1\xe4\xba\xa7)'), (1, b'\xe9\x9d\xa2\xe6\x8e\x88(\xe5\x91\xa8\xe6\x9c\xab)'), (2, b'\xe7\xbd\x91\xe7\xbb\x9c\xe7\x8f\xad')], verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('semester', models.PositiveSmallIntegerField(verbose_name=b'\xe5\xad\xa6\xe6\x9c\x9f')),
                ('start_date', models.DateField(verbose_name=b'\xe5\xbc\x80\xe7\x8f\xad\xe6\x97\xa5\xe6\x9c\x9f')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name=b'\xe7\xbb\x93\xe4\xb8\x9a\xe6\x97\xa5\xe6\x9c\x9f')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name=b'\xe6\xa0\xa1\xe5\x8c\xba')),
            ],
            options={
                'verbose_name': '\u73ed\u7ea7',
                'verbose_name_plural': '\u73ed\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('period', models.PositiveSmallIntegerField(verbose_name=b'\xe5\x91\xa8\xe6\x9c\x9f(\xe6\x9c\x88)')),
                ('outline', models.TextField()),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8868',
                'verbose_name_plural': '\u8bfe\u7a0b\u8868',
            },
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.PositiveSmallIntegerField(verbose_name=b'\xe7\xac\xac\xe5\x87\xa0\xe8\x8a\x82(\xe5\xa4\xa9)')),
                ('has_homework', models.BooleanField(default=True)),
                ('homework_title', models.CharField(blank=True, max_length=128, null=True)),
                ('homework_content', models.TextField(blank=True, null=True)),
                ('outline', models.TextField(verbose_name=b'\xe6\x9c\xac\xe8\x8a\x82\xe8\xaf\xbe\xe7\xa8\x8b\xe5\xa4\xa7\xe7\xba\xb2')),
                ('date', models.DateField(auto_now_add=True)),
                ('from_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7')),
            ],
            options={
                'verbose_name_plural': '\u4e0a\u8bfe\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('qq', models.CharField(max_length=64, unique=True)),
                ('qq_name', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('source', models.SmallIntegerField(choices=[(0, b'\xe8\xbd\xac\xe4\xbb\x8b\xe7\xbb\x8d'), (1, b'QQ\xe7\xbe\xa4'), (2, b'\xe5\xae\x98\xe7\xbd\x91'), (3, b'\xe7\x99\xbe\xe5\xba\xa6\xe6\x8e\xa8\xe5\xb9\xbf'), (4, b'51CTO'), (5, b'\xe7\x9f\xa5\xe4\xb9\x8e'), (6, b'\xe5\xb8\x82\xe5\x9c\xba\xe6\x8e\xa8\xe5\xb9\xbf')])),
                ('referral_from', models.CharField(blank=True, max_length=64, null=True, verbose_name=b'\xe8\xbd\xac\xe4\xbb\x8b\xe7\xbb\x8d\xe4\xba\xbaqq')),
                ('content', models.TextField(verbose_name=b'\xe5\x92\xa8\xe8\xaf\xa2\xe8\xaf\xa6\xe6\x83\x85')),
                ('status', models.SmallIntegerField(choices=[(0, b'\xe5\xb7\xb2\xe6\x8a\xa5\xe5\x90\x8d'), (1, b'\xe6\x9c\xaa\xe6\x8a\xa5\xe5\x90\x8d')], default=1)),
                ('memo', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consult_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name=b'\xe5\x92\xa8\xe8\xaf\xa2\xe8\xaf\xbe\xe7\xa8\x8b')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u8868',
                'verbose_name_plural': '\u5ba2\u6237\u8868',
            },
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name=b'\xe8\xb7\x9f\xe8\xbf\x9b\xe5\x86\x85\xe5\xae\xb9')),
                ('intention', models.SmallIntegerField(choices=[(0, b'2\xe5\x91\xa8\xe5\x86\x85\xe6\x8a\xa5\xe5\x90\x8d'), (1, b'1\xe4\xb8\xaa\xe6\x9c\x88\xe5\x86\x85\xe6\x8a\xa5\xe5\x90\x8d'), (2, b'\xe8\xbf\x91\xe6\x9c\x9f\xe6\x97\xa0\xe6\x8a\xa5\xe5\x90\x8d\xe8\xae\xa1\xe5\x88\x92'), (3, b'\xe5\xb7\xb2\xe5\x9c\xa8\xe5\x85\xb6\xe5\xae\x83\xe6\x9c\xba\xe6\x9e\x84\xe6\x8a\xa5\xe5\x90\x8d'), (4, b'\xe5\xb7\xb2\xe6\x8a\xa5\xe5\x90\x8d'), (5, b'\xe5\xb7\xb2\xe6\x8b\x89\xe9\xbb\x91')])),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u8ddf\u8fdb\u8bb0\u5f55',
                'verbose_name_plural': '\u5ba2\u6237\u8ddf\u8fdb\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_agreed', models.BooleanField(default=False, verbose_name=b'\xe5\xad\xa6\xe5\x91\x98\xe5\xb7\xb2\xe5\x90\x8c\xe6\x84\x8f\xe5\x90\x88\xe5\x90\x8c\xe6\x9d\xa1\xe6\xac\xbe')),
                ('contract_approved', models.BooleanField(default=False, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe5\xb7\xb2\xe5\xae\xa1\xe6\xa0\xb8')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '\u62a5\u540d\u8868',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=500, verbose_name=b'\xe6\x95\xb0\xe9\xa2\x9d')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '\u7f34\u8d39\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('menus', models.ManyToManyField(blank=True, to='crm.Menu')),
            ],
            options={
                'verbose_name_plural': '\u89d2\u8272',
            },
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.SmallIntegerField(choices=[(0, b'\xe5\xb7\xb2\xe7\xad\xbe\xe5\x88\xb0'), (1, b'\xe8\xbf\x9f\xe5\x88\xb0'), (2, b'\xe7\xbc\xba\xe5\x8b\xa4'), (3, b'\xe6\x97\xa9\xe9\x80\x80')], default=0)),
                ('score', models.SmallIntegerField(choices=[(100, b'A+'), (90, b'A'), (85, b'B+'), (80, b'B'), (75, b'B-'), (70, b'C+'), (60, b'C'), (40, b'C-'), (-50, b'D'), (-100, b'COPY'), (0, b'N/A')], default=0)),
                ('memo', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Enrollment')),
            ],
            options={
                'verbose_name_plural': '\u5b66\u4e60\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('roles', models.ManyToManyField(blank=True, null=True, to='crm.Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name=b'\xe6\x89\x80\xe6\x8a\xa5\xe8\xaf\xbe\xe7\xa8\x8b'),
        ),
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe9\xa1\xbe\xe9\x97\xae'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='enrolled_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name=b'\xe6\x89\x80\xe6\x8a\xa5\xe7\x8f\xad\xe7\xba\xa7'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='crm.Tag'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='crm.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('student', 'course_record')]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('customer', 'enrolled_class')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('from_class', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('branch', 'course', 'semester')]),
        ),
    ]
