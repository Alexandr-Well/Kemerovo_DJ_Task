from django.db import models

from app_users.models import CustomUser


class Notice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    crated_at = models.DateTimeField("crated at", auto_now_add=True)
    title = models.CharField('Title:', max_length=255, blank=False)
    text = models.TextField('Notice:', blank=False)

    class META:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notice'

    def __str__(self):
        return self.title
