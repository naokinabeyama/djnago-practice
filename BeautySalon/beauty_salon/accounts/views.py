from pipes import Template
from django.shortcuts import redirect, render
from .forms import(
    RegistForm, UserLoginForm, UserUpdateForm
)
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Users
from django.urls import reverse, reverse_lazy




# ホーム画面
class HomeView(TemplateView):
    template_name = 'home.html'


# ユーザー登録
class UserRegistView(CreateView):
    template_name = 'user_regist.html'
    form_class = RegistForm


# ログイン
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm


# ログアウト
class UserLogoutView(LogoutView):
    pass


# マイページ
class UserMyPageView(LoginRequiredMixin, DetailView):
  template_name = 'mypage.html'
  model = Users

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_detail = Users.objects.filter(
      pk = self.request.user.id
    )
    context['user_detail'] = user_detail
    return context


# ユーザー更新
class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'user_update.html'
    model = Users
    form_class = UserUpdateForm

    def get_success_message(self, cleaned_data):
        return cleaned_data.get('username') + 'さんの情報を更新しました'


# ユーザー退会
class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user_delete.html'
    model = Users
    success_url = reverse_lazy('accounts:home')
