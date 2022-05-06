from django.urls import path
from .views import (
    HomeView, UserRegistView, UserLoginView, UserLogoutView, UserMyPageView, UserUpdateView, UserDeleteView
)

app_name = 'accounts'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('user_regist/', UserRegistView.as_view(), name='user_regist'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    path('mypage/<int:pk>', UserMyPageView.as_view(), name='mypage'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('user_delete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
]
