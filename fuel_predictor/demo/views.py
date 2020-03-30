from django.shortcuts import render
from .forms import *
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def admin(request):
    return render(request, 'admin.html')


def client_profile(request):
    return render(request, 'client_profile.html')


def fuel_quote(request):
    return render(request, 'fuel_quote.html')


def fuel_hist(request):
    return render(request, 'fuel_hist.html')


def subscribe(request):
    # if POST request, process the form data
    if request.method == 'POST':
        print("2")
        form = SubscribeForm(request.POST)
        print(form['fullname'].value())
        # check whether it's valid
        if form.is_valid():
            return HttpResponseRedirect('thanks')

    # if GET request, create a blank form
    else:
        print("1")
        form = SubscribeForm()

    return render(request, 'subscribe.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
