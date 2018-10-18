from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from .models import Contact


@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.message = form.cleaned_data['message']

            contact.save()

            messages.info(request, 'Thank you (TBD)')
            form = ContactForm()  # make it clean again

    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

# def home(request):
    # return render(request, 'home.html')
