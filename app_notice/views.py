from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.shortcuts import redirect
from django.views.generic import FormView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app_notice.forms import NoticeForm
from app_notice.models import Notice
from app_users.models import CustomUser
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView


class MainPage(LoginRequiredMixin, FormMixin, ListView):
    paginate_by = 3
    template_name = 'notice/main_notice_page.html'
    model = Notice
    context_object_name = 'notice'
    queryset = Notice.objects.filter(
        is_public=True).select_related('user').only('user__username').order_by('-crated_at')
    form_class = NoticeForm
    login_url = 'login'
    redirect_field_name = 'main'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('main')


class UserNotice(LoginRequiredMixin, FormView):
    template_name = 'notice/user_notice_page.html'
    context_object_name = 'users'
    form_class = NoticeForm

    def get_context_data(self, **kwargs):
        notice = Notice.objects.filter(
            user_id=self.request.user.pk).select_related('user').only('user__username').order_by('-crated_at')[:20]
        users = cache.get('users')
        if not users:
            users = CustomUser.objects.filter(is_active=True)
            cache.set('users', users, 60)
        kwargs.update({
            'notice': notice,
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('users_notice')


class NoticeDetail(DetailView):
    model = Notice
    template_name = 'notice/notice_page_detail.html'
