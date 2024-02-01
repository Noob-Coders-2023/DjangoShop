from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label='نام',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20',
                                                             'placeholder': 'نام و نام خانوادگی خود را وارد کنید.'})
                               )
    email = forms.EmailField(label='ایمیل',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'placeholder': 'یک ایمیل معتبر وارد کنید.'})
                             )
    message = forms.CharField(label='پیام شما',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'placeholder': 'متن پیام خود را وارد کنید.'})
                              )
