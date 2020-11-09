from django.shortcuts import render


def home_view(request):
    """
    View to return home page
    """
    return render(request, "home.html")
