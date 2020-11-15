from django.shortcuts import get_object_or_404, render
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
        "home_page": "home",
        "form": form,
        "specialties": specialties
        # "emailjs_user": # emailjs_user
    }
    return render(request, "home.html", context)


def specialty_detail_view(request, pk):
    """
    View to return detail about each specialty
    """

    # Return the list of all sub-specialty matching the specialty id
    specialty = get_object_or_404(Specialty, pk=pk)
    sub_specialties = ListForSpecialty.objects.all().filter(related_specialty=specialty)

    context = {
        "page_title": specialty,
        "specialty": specialty,
        "sub_specialties": sub_specialties
    }

    return render(request, "specialty_detail.html", context)
