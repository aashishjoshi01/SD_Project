from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import date
from .forms import *
import re


# Create your views here.


def login(request):
    if request.method == 'POST':
        print("1")
        data = request.POST.copy()
        # print(data)
        username = data.get('username')
        password = data.get('password')

        users = {'Sharath123': 'Password123', 'AashishJoshi': 'Joshi1996', 'Praneeth': 'Pragada98'}

        # Username and pwd is compared to existing data to validate the authenticity of the user
        for user in users:

            if username == user and password == users[user]:
                return HttpResponseRedirect('fuel_quote')
        else:
            message = 'Unable to verify user. Please check Username and Password'
            return render(request, 'login.html', {'message': message, 'uname': username})

    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # print(data)
        uname = data.get('username')
        pwd = data.get('password')

        existing_users = ['Sharath123', 'Aashish96']

        # Username should be unique. Comparing it with other existing usernames
        if uname not in existing_users:
            if str.isalnum(uname) and str.isalnum(pwd):
                if str.upper(pwd) != pwd and str.lower(pwd) != pwd:
                    if len(uname) > 7:
                        if len(pwd) > 7:
                            return HttpResponseRedirect('login')
                        else:
                            message = 'Password must contain at least 8 characters'
                            return render(request, 'signup.html', {'message': message, 'uname': uname})
                    else:
                        message = 'Username must contain atleast 8 characters'
                        return render(request, 'signup.html', {'message': message, 'uname': uname})
                else:
                    message = 'Password must contain both uppercase and lowercase alphabets'
                    return render(request, 'signup.html', {'message': message, 'uname': uname})
            else:
                message = 'Username and password can contain only alphabets & numbers'
                return render(request, 'signup.html', {'message': message, 'uname': uname})
        else:
            message = 'Username is already taken. Please choose another one'
            return render(request, 'signup.html', {'message': message, 'uname': uname})

    else:
        return render(request, 'signup.html')


def admin(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # print(data)
        srf = data.get('srf')
        baseprice = data.get('baseprice')
        profit = data.get('profit')

        try:
            float(srf)
            try:
                float(baseprice)
                try:
                    float(profit)
                    return HttpResponseRedirect('fuel_quote')
                except ValueError:
                    message = 'Profit should be an integer'
                    return render(request, 'admin.html',
                                  {'message': message, 'srf': srf, 'baseprice': baseprice, 'profit': profit})
            except ValueError:
                message = 'Base price should be an integer'
                return render(request, 'admin.html',
                              {'message': message, 'srf': srf, 'baseprice': baseprice, 'profit': profit})
        except ValueError:
            message = 'Seasonal rate fluctuation is an integer'
            return render(request, 'admin.html',
                          {'message': message, 'srf': srf, 'baseprice': baseprice, 'profit': profit})
    else:
        return render(request, 'admin.html')


def client_profile(request):
    if request.method == "POST":
        data = request.POST.copy()
        fname = data.get('fname')
        addr1 = data.get('address1')
        addr2 = data.get('address2')
        city = data.get('city')
        state = data.get('state')
        zipcode = data.get('zipcode')

        print("State  - ", state)

        pattern = re.compile("^[A-Za-z ]+$")

        if pattern.match(fname):
            if str.isalpha(city):
                if len(state) != 0:
                    if str.isnumeric(zipcode):
                        return HttpResponseRedirect('fuel_quote')
                    else:
                        message = 'Zipcode can only contain numbers'
                        return render(request, 'client_profile.html',
                                      {'message': message, 'fname': fname, 'addr1': addr1, 'addr2': addr2, 'city': city,
                                       'state': state, 'zipcode': zipcode})
                else:
                    message = "Please select a State"
                    return render(request, 'client_profile.html',
                                  {'message': message, 'fname': fname, 'addr1': addr1, 'addr2': addr2, 'city': city,
                                   'state': state, 'zipcode': zipcode})
            else:
                message = 'City field can contain only alphabets'
                return render(request, 'client_profile.html',
                              {'message': message, 'fname': fname, 'addr1': addr1, 'addr2': addr2, 'city': city,
                               'state': state, 'zipcode': zipcode})
        else:
            message = 'Full Name can contain only alphabets'
            return render(request, 'client_profile.html',
                          {'message': message, 'fname': fname, 'addr1': addr1, 'addr2': addr2, 'city': city,
                           'state': state, 'zipcode': zipcode})

    else:
        return render(request, 'client_profile.html')


def fuel_quote(request):
    if request.method == 'POST':

        base_price = 2

        data = request.POST.copy()

        gallons = data.get("gallons")
        address = data.get("address")
        deliveryDate = data.get("date")

        try:
            gallons = float(gallons)
            if len(address) != 0:
                today = date.today()
                d3 = today.strftime("%Y-%m-%d")
                d3 = str(d3)

                print(deliveryDate)
                print(d3)

                if d3 < deliveryDate:
                    return render(request, 'fuel_quote.html',
                                  {'gallons': gallons, 'address': address, 'date': deliveryDate, 'visible': 'visible',
                                   'price': base_price, 'amount': base_price * gallons})
                else:
                    message = 'Delivery Date must be in the future'
                    return render(request, 'fuel_quote.html',
                                  {'message': message, 'gallons': gallons, 'address': address, 'date': deliveryDate})
            else:
                message = 'Address field cannot be empty'
                return render(request, 'fuel_quote.html',
                              {'message': message, 'gallons': gallons, 'address': address, 'date': deliveryDate})
        except ValueError:
            message = 'Gallons must be an integer'
            return render(request, 'fuel_quote.html',
                          {'message': message, 'gallons': gallons, 'address': address, 'date': deliveryDate})

    else:
        return render(request, 'fuel_quote.html', {'visible': 'hidden'})


def fuel_hist(request):
    rows = [[12, 'Texas', '01 / 02 / 2020', 3.25, 39],
            [19, 'California', '02 / 18 / 2020', 3.3, 62.7],
            [17, 'Texas ', '02 / 28 / 2020', 2.9, 49.3],
            [10, 'Florida', '03 / 06 / 2020', 3.5, 35],
            [16, 'Texas', '03 / 07 / 2020', 3.2, 51.2]]

    return render(request, 'fuel_hist.html', {'rows': rows})
