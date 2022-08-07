import logging

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin
from django.urls import reverse

from loguru import logger

log = logging.getLogger('django')
logger.add('debug1.log', format='{time}{level}{message}', level="INFO", rotation='2MB', compression='zip')


class CustomUser(AbstractUser, PermissionsMixin):
    """Модель юзера"""
    birthday = models.DateField('Date of birth: ', blank=True, null=True)
    # фио лучше разделить по разным полям, у такого подхода больше приемуществ, бд более "нормальная", фильтрация гибче
    first_name = models.TextField("first name", blank=True)
    last_name = models.TextField("last name", blank=True)
    fathers_name = models.TextField("fathers name", blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d/', null=True, blank=True)
    status = models.TextField("status", max_length=140, default="")
    verification = models.BooleanField('verification', default=False)

    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUser"

    def get_absolute_url(self):
        return reverse('user_info')


class CustomGroup(Group):
    """Модель групп"""

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Group"
        ordering = ['name']
