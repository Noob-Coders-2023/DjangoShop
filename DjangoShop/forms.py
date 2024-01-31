from django import forms
from django.contrib.auth import get_user_model
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password = forms.CharField(label='رمز عبور',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
                               validators=[
                                   validators.MaxLengthValidator(limit_value=20, message='نام کاربری نباید بیش از 20 '
                                                                                         'کارکتر باشد.')
                               ])
    email = forms.EmailField(label='آدرس ایمیل',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'آدرس ایمیل'}),
                             validators=[
                                 validators.EmailValidator('ایمیل نامعتبر است.')
                             ])
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username)

        if query.exists():
            raise forms.ValidationError('نام کاربری تکراری است.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email)

        if query.exists():
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است.')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('رمزهای ورود مطابقت ندارند.')
        return data
