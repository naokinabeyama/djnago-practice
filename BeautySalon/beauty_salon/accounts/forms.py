from django import forms
from .models import Users
from datetime import date
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm


# ユーザー登録フォーム
class RegistForm(forms.ModelForm):
    gender_choice = [
        (1, '男性'),
        (2, '女性'),
        (0, 'その他')
    ]

    # ユーザーネーム
    username = forms.CharField(label='ユーザーネーム', max_length=50)
    # 名前
    first_name = forms.CharField(label='名前', max_length=50)
    # 苗字
    last_name = forms.CharField(label="苗字", max_length=50)
    # メールアドレス
    email = forms.EmailField(label='メールアドレス', max_length=150)
    # 誕生日
    today = date.today()
    past = int(today.year - 100)
    birthday = forms.DateField(label='誕生日', widget=forms.SelectDateWidget(years=[x for x in range(past, today.year)]))
    # 性別
    gender = forms.ChoiceField(label='性別', widget=forms.RadioSelect, choices=gender_choice, initial=1)
    # パスワード
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
      model = Users
      fields = [
          'username',
          'first_name',
          'last_name',
          'email',
          'birthday',
          'gender',
          'password'
      ]
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


# ログインフォーム
class UserLoginForm(AuthenticationForm):
    # このusernameは一意を識別するもの(emailをunique=Trueにしている)
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
  

# ユーザー更新フォーム
class UserUpdateForm(forms.ModelForm):
    gender_choice = [
        (1, '男性'),
        (2, '女性'),
        (0, 'その他')
    ]

    # ユーザーネーム
    username = forms.CharField(label='ユーザーネーム', max_length=50)
    # 名前
    first_name = forms.CharField(label='名前', max_length=50)
    # 苗字
    last_name = forms.CharField(label="苗字", max_length=50)
    # メールアドレス
    email = forms.EmailField(label='メールアドレス', max_length=150)
    # 誕生日
    today = date.today()
    past = int(today.year - 100)
    birthday = forms.DateField(label='誕生日', widget=forms.SelectDateWidget(years=[x for x in range(past, today.year)]))
    # 性別
    gender = forms.ChoiceField(label='性別', widget=forms.RadioSelect, choices=gender_choice, initial=1)

    class Meta:
        model = Users
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'birthday',
            'gender',
        ]
    
