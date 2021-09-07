from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import ProfileForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully')

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profile.html'
    context = {
        "profile": profile,
        "form": form,
        "orders": orders,
        "check_profile": True
    }

    return render(request, template, context)
