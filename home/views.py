from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from .models import Specialty, ListForSpecialty


def home_view(request):
    """
    View to return home page
    """
    form = ContactForm()

    # emailjs_user = settings.EMAILJS_USER
    specialties = Specialty.objects.all()

    context = {
        "page_title": "Home",
        "form": form,
        "specialties": specialties
        # "emailjs_user": # emailjs_user
    }
    return render(request, "home.html", context)
