# -*- coding:utf-8 -*-

import uuid

from django.db import models


class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, verbose_name='ID')
    task_name = models.CharField(max_length=32, unique=True, verbose_name='任务名')


