from django.shortcuts import render
from .models import ContactUs
from .forms import ContactForm


# Create your views here.

def contact_us(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('message')
        new_contact = ContactUs.objects.create(full_name=full_name, email=email, message=message)

    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact_us.html', context)
