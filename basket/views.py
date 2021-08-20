from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ This returns the index page """

    return render(request, "basket/basket.html")
