from time import timezone
from django.shortcuts import render, HttpResponse
from . import forms
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.utils import timezone
from . import models


# Create your views here.


class main(FormView):
    form_class = forms.ContactForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def test(request):
    return render(request, 'main/test.html')

def storage(request):
    contacts=models.Contact.objects.all()
    return render(request, 'main/storage.html', {'contacts': contacts})
