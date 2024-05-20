# views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Contact
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'sound/contact_form.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)  # Show 10 contacts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sound/contact_list.html', {'page_obj': page_obj})
