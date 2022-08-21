from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from app_users.forms import RegistrationUserForm, LoginUserForm
import logging
from loguru import logger
from django.contrib.auth import login as auth_login, logout

from app_users.models import CustomUser

log = logging.getLogger('django')
logger.add('debug1.log', format='{time}{level}{message}', level="INFO", rotation='2MB', compression='zip')


class RegisterUser(CreateView):
    """ форма для создания юзера
    form_valid авторизирует только что созданного юзера
    """
    form_class = RegistrationUserForm
    template_name = "user/add_user.html"
    success_url = reverse_lazy("main")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        logger.info(f"{self.request.user.username} registered")
        return redirect('main')


class LoginUser(LoginView):
    """ форма для входа под учетную запись"""
    form_class = LoginUserForm
    template_name = "user/user_auth.html"

    success_url = reverse_lazy("main")

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        logger.info(f"{self.request.user.username} logged in")
        return HttpResponseRedirect(self.get_success_url())


def logout_user(request):
    """
    logout
    """
    logout(request)
    logger.info(f"{request.user.username} logged out")
    return redirect('login')


class ViewUserInfo(LoginRequiredMixin, TemplateView):
    """
    главная страница юзера
    """
    template_name = 'user/user_info.html'
    login_url = 'login'
    redirect_field_name = ''


class ViewOthersUserInfo(LoginRequiredMixin, TemplateView):
    template_name = 'user/other_user_info.html'
    login_url = 'login'
    redirect_field_name = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({
            'user': CustomUser.objects.filter(pk=self.kwargs['pk']).first()
        })
        return super().get_context_data(**kwargs)


class EditUserInfo(LoginRequiredMixin, UpdateView):
    """
    изменение информации о юзере
    """
    login_url = 'login'
    redirect_field_name = 'user_info'

    template_name = 'user/cng_user_info.html'
    model = CustomUser
    fields = ['status', 'first_name',  'last_name', 'fathers_name', 'birthday', 'username', 'email', 'file']

    def get_object(self):
        return self.request.user
