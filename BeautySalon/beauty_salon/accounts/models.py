from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.urls import reverse_lazy
from store.models import Reserves


class UserManager(BaseUserManager):
    # ユーザー
    def create_user(self, username, email, password=None):
        # メールアドレス判定
        if not email:
          raise ValueError('Email Error')
        
        user = self.model(
            username = username,
            email = email
        )
        # パスワードをハッシュ化
        user.set_password(password)
        # 保存
        user.save(using=self._db)
        return user
    
    # 管理者
    def create_superuser(self, username, email, password=None):
        user = self.model(
            username = username,
            email = email
        )
        # パスワードをハッシュ化
        user.set_password(password)
        # 管理者権限
        user.is_staff = True
        # ログイン権限
        user.is_active=True
        # 全ての権限
        user.is_superuser=True
        # 保存
        user.save(using=self._db)
        return user




class Users(AbstractBaseUser, PermissionsMixin):
    # ユーザーネーム
    username = models.CharField(verbose_name='ユーザーネーム', max_length=50, unique=True)
    # 名前
    first_name = models.CharField(verbose_name='名前', max_length=50)
    # 苗字
    last_name = models.CharField(verbose_name='苗字', max_length=50)
    # メールアドレス
    email = models.EmailField(verbose_name='メールアドレス', max_length=150, unique=True)
    # 誕生日
    birthday = models.DateField(verbose_name='誕生日', blank=True, null=True)
    # 性別
    gender = models.IntegerField(verbose_name='性別', blank=True, null=True)
    # ログイン権限
    is_active = models.BooleanField(default=True)
    # 管理者権限
    is_staff = models.BooleanField(default=False)
    # 予約日
    # reserves = models.ForeignKey(
    #     Reserves,
    #     on_delete=models.CASCADE
    # )

    # 一意の識別子
    USERNAME_FIELD = 'email'
    # 管理者が管理コマンド上（ターミナル等）でユーザーを作成する時に表示されるリスト
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name_plural = 'ユーザー一覧'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse_lazy('accounts:mypage', kwargs={'pk':self.pk})
  
