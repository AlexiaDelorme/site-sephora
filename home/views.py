from django.shortcuts import get_object_or_404, render
from django.conf import settings
from .forms import ContactForm
from .models import Specialty, SubSpecialty, ListForSubSpecialty


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
    sub_specialties = SubSpecialty.objects.all().filter(related_specialty=specialty)

    context = {
        "page_title": specialty.name,
        "specialty": specialty,
        "sub_specialties": sub_specialties
    }

    return render(request, "specialty_detail.html", context)


def sub_specialty_detail_view(request, pk):
    """
    View to return detail about each sub specialty
    """

    # Return the list of all sub-specialty matching the specialty id
    sub_specialty = get_object_or_404(SubSpecialty, pk=pk)
    sub_specialty_list = ListForSubSpecialty.objects.all().filter(related_sub_specialty=sub_specialty)

    context = {
        "page_title": sub_specialty.name,
        "sub_specialty": sub_specialty,
        "sub_specialty_list": sub_specialty_list
    }

    return render(request, "sub_specialty_detail.html", context)
