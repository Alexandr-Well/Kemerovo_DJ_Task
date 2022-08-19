from django.core.cache import cache

from app_users.models import CustomUser


def get_users(request):
    users = cache.get('users')
    if not users:
        users = CustomUser.objects.filter(is_active=True).exclude(pk=request.user.pk)
        cache.set('users', users, 60)
    return {'users': users}
