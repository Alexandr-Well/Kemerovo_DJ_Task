from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views.generic import FormView, DetailView
from app_notice.forms import NoticeForm
from app_notice.models import Notice
from .utils import make_pagination


class MainPage(LoginRequiredMixin, FormView):
    template_name = 'notice/main_notice_page.html'
    form_class = NoticeForm
    login_url = 'login'
    redirect_field_name = 'main'

    def get_context_data(self, **kwargs):
        paginator = Paginator(
            Notice.objects.filter(is_public=True).select_related('user').only('user__username').order_by(
                '-crated_at'), 20)
        kwargs.update(make_pagination(page=self.request.GET.get('page'), paginator=paginator))
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('main')


class UserNotice(LoginRequiredMixin, FormView):
    template_name = 'notice/user_notice_page.html'
    form_class = NoticeForm

    def get_context_data(self, **kwargs):
        paginator = Paginator(Notice.objects.filter(
            user_id=self.request.user.pk).select_related('user').only('user__username').order_by('-crated_at'), 10)
        kwargs.update(make_pagination(page=self.request.GET.get('page'), paginator=paginator))
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('users_notice')


class NoticeDetail(DetailView):
    model = Notice
    template_name = 'notice/notice_page_detail.html'
