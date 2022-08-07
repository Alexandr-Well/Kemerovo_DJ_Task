from django.contrib import admin

from app_notice.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'crated_at', 'title'
    )
