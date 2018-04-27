# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-09 15:39
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='邮箱')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('image', models.ImageField(blank=True, default='default.png', max_length=128, null=True, upload_to='user_images/%Y/%m/%d', verbose_name='头像')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='是否为超级管理员')),
                ('is_staff', models.BooleanField(default=False, verbose_name='是否为管理员')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('is_online', models.BooleanField(default=False, verbose_name='是否在线')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'permissions': (('view_user_list', '访问用户列表'), ('view_user', '查看用户'), ('add_user', '添加用户'), ('change_user', '编辑用户'), ('delete_user', '删除用户')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='用户组名')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '用户组',
                'verbose_name_plural': '用户组',
                'permissions': (('view_usergroup_list', '访问用户组列表'), ('view_usergroup', '查看用户组'), ('add_usergroup', '添加用户组'), ('change_usergroup', '编辑用户组'), ('delete_usergroup', '删除用户组')),
            },
        ),
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField(verbose_name='IP地址')),
                ('login_time', models.DateTimeField(auto_now_add=True, verbose_name='登陆时间')),
                ('logout_time', models.DateTimeField(blank=True, null=True, verbose_name='登出时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '用户登陆日志',
                'verbose_name_plural': '用户登陆日志',
                'permissions': (('view_userloginlog_list', '访问用户登录日志列表'), ('view_userloginlog', '查看用户登录日志'), ('add_userloginlog', '添加用户登录日志'), ('change_userloginlog', '编辑用户登录日志'), ('delete_userloginlog', '删除用户登录日志')),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='user_group',
            field=models.ManyToManyField(related_name='user_group', to='accounts.UserGroup', verbose_name='用户组'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]