from django.shortcuts import render

# Create your views here.


def index(request):
    """ This returns the index page """
    request.session["basket"] = []
    return render(request, "home/index.html")
