from django import forms


class UserEditProfileForm(forms.Form):
    first_name = forms.CharField(label='نام',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'نام خود را وارد نمایید.'}),
                                 )

    last_name = forms.CharField(label='نام خانوادگی',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'نام خانوادگی خود را وارد نمایید.'}),
                                )

    email = forms.EmailField(label='ایمیل',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'ایمیل خود را وارد نمایید.'}),
                             )
