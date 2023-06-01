from django.urls import path
from .views import HomeView, ContactView, Contact

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/create', Contact, name='contact_create'),
]
