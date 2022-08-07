from django.core.cache import cache
from django.shortcuts import redirect
from django.views.generic import FormView, DetailView

from app_notice.forms import NoticeForm
from app_notice.models import Notice
from app_users.models import CustomUser


class MainPage(FormView):
    template_name = 'notice/main_notice_page.html'
    context_object_name = 'users'
    form_class = NoticeForm

    def get_context_data(self, **kwargs):
        notice = Notice.objects.all().select_related('user').only('user__username').order_by('-crated_at')[:20]
        users = cache.get('users')
        if not users:
            users = CustomUser.objects.filter(is_active=True)
            cache.set('users', users, 60)
        kwargs.update({
            'users': users,
            'notice': notice,
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('main')


class NoticeDetail(DetailView):
    model = Notice
    template_name = 'notice/notice_page_detail.html'


