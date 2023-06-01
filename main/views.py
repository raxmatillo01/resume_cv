from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .models import ContactMessageModel
from .forms import ContactForm
import requests

class HomeView(TemplateView):
    template_name = 'index.html'




class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context


def Contact(request):
    contact = ContactMessageModel.objects.all()
    context = {
        'contact': contact,
    }
    if request.method == "POST":
        ContactMessageModel.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message"),
        )
        token = "5949655720:AAF9fUVW8J8UrP00KzMGPcqmtdb-y6vYSmA"
        text = "Sizga xabar yuborishdi: \n\n Ism: " + request.POST.get('name') + '\n Email: ' + str(request.POST.get("email")) + '\n Telefon raqam: ' + str(
            request.POST.get("phone")) + '\n Xabari: ' + request.POST.get('message')
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(640145065) + '&text=' + text)
    return render(request, 'contact.html', context)