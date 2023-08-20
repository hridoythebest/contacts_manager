from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import Form, ModelForm
from .models import Contact
from .forms import ContactForm

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/list.html', {'contacts': contacts})

def create_contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save()
        return HttpResponseRedirect('/')
    return render(request, 'contact/create.html', {'form': form})

def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'contact/edit.html', {'form': form, 'contact': contact})

def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return HttpResponseRedirect('/')