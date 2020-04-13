import hashlib
import re
import sqlite3
from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def check_login(request):
    try:
        username = request.COOKIES['username']
        password = request.COOKIES['password']

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')

        cur = conn.cursor()

        cur.execute("select * from login")

        for user in cur.fetchall():
            if user[0] == username and user[1] == password:
                return True
        else:
            return False

        # Praneeth      -   Pragada98
        # Aashish       -   Joshi1996
        # Sharath123    -   Password123

    except KeyError:
        return False


def check_admin(request):
    username = request.COOKIES['username']

    conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
    cur = conn.cursor()

    cur.execute("select * from login where username = ?", (username,))
    row = cur.fetchone()

    if row[2] == 'Admin':
        return True
    else:
        return False


def login(request):
    if request.method == 'POST':

        data = request.POST.copy()
        # print(data)
        username = data.get('username')
        password = data.get('password')
        hash_pwd = hashlib.md5(password.encode('utf-8')).hexdigest()

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')

        cur = conn.cursor()

        cur.execute("select * from login")

        # Username and pwd is compared to existing data to validate the authenticity of the user
        for user in cur.fetchall():
            if username == user[0] and hash_pwd == user[1]:
                # request.session.set_cookie('username', username)

                if user[2] == 'Admin':
                    response = HttpResponseRedirect('admin')
                else:
                    if user[3] == 0:
                        response = HttpResponseRedirect('client_profile')
                    else:
                        response = HttpResponseRedirect('fuel_quote')

                response.set_cookie('username', username)
                response.set_cookie('password', hash_pwd)

                return response
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
        hash_pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
        flag = 0

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
        cur = conn.cursor()

        cur.execute("select * from login")

        # existing_users = ['Sharath123', 'Aashish96']

        # Username should be unique. Comparing it with other existing usernames

        for user in cur.fetchall():
            if user[0] == uname:
                flag = 1

        if flag == 0:
            if str.isalnum(uname) and str.isalnum(pwd):
                if str.upper(pwd) != pwd and str.lower(pwd) != pwd:
                    if len(uname) > 7:
                        if len(pwd) > 7:
                            response = HttpResponseRedirect('login')
                            response.set_cookie('username', uname)
                            response.set_cookie('password', hash_pwd)

                            cur.execute("insert into login (username, password, access, flag) values(?,?,?,?)",
                                        (uname, hash_pwd, 'User', 0))
                            conn.commit()

                            return response
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

        if not check_login(request):
            return HttpResponseRedirect('login')

        if not check_admin(request):
            return HttpResponseRedirect('fuel_quote')

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

                    conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
                    cur = conn.cursor()

                    cur.execute("update admin set srf = ?, baseprice = ?, profit = ?", (srf, baseprice, profit))
                    conn.commit()
                    conn.close()

                    message = "Update Successful"

                    return render(request, 'admin.html',
                                  {'message': message, 'srf': srf, 'baseprice': baseprice, 'profit': profit})
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
        if check_login(request):

            if not check_admin(request):
                return HttpResponseRedirect('fuel_quote')

            conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
            cur = conn.cursor()

            cur.execute("select * from admin")
            row = cur.fetchone()

            conn.close()

            srf = row[0]
            baseprice = row[1]
            profit = row[2]

            return render(request, 'admin.html', {'srf': srf, 'baseprice': baseprice, 'profit': profit})
        else:
            return HttpResponseRedirect('login')


def client_profile(request):
    if request.method == "POST":

        if not check_login(request):
            return HttpResponseRedirect('login')

        data = request.POST.copy()

        username = request.COOKIES['username']

        fname = data.get('fname')
        addr1 = data.get('address1')
        addr2 = data.get('address2')
        city = data.get('city')
        state = data.get('state')
        zipcode = data.get('zipcode')

        pattern = re.compile("^[A-Za-z ]+$")

        flag = 0

        if pattern.match(fname):
            if str.isalpha(city):
                if len(state) != 0:
                    if str.isnumeric(zipcode):

                        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
                        cur = conn.cursor()

                        cur.execute("select * from profile")

                        for prof in cur.fetchall():
                            if prof[0] == username:
                                flag = 1
                                cur.execute(
                                    "update profile set username = ?, fullname = ?, address1 = ?, address2 = ?, "
                                    "city = ?, state = ?, zipcode = ?",
                                    (username, fname, addr1, addr2, city, state, zipcode))

                        if flag == 0:
                            cur.execute(
                                "insert into profile (username, fullname, address1, address2, city, state, zipcode) "
                                "values(?,?,?,?,?,?,?)",
                                (username, fname, addr1, addr2, city, state, zipcode))

                        conn.commit()

                        cur.execute("update login set flag = ? where username = ?", (1, username))

                        conn.commit()

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
        if check_login(request):
            username = request.COOKIES['username']

            conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')

            cur = conn.cursor()

            cur.execute("select * from profile")

            for profile in cur.fetchall():
                if profile[0] == username:
                    fname = profile[1]
                    addr1 = profile[2]
                    addr2 = profile[3]
                    city = profile[4]
                    state = profile[5]
                    zipcode = profile[6]

                    return render(request, 'client_profile.html',
                                  {'fname': fname, 'addr1': addr1, 'addr2': addr2, 'city': city,
                                   'state': state, 'zipcode': zipcode})
            else:
                return render(request, 'client_profile.html')
        else:
            return HttpResponseRedirect('login')


def fuel_quote(request):
    if request.POST.get("getprice"):
        if not check_login(request):
            return HttpResponseRedirect('login')

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

                # print(deliveryDate)
                # print(d3)

                if d3 < deliveryDate:

                    # Code to calculate the fuel price

                    if gallons > 1000:
                        gallons_requested_factor = 2
                    else:
                        gallons_requested_factor = 3

                    conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')

                    cur = conn.cursor()

                    username = request.COOKIES['username']

                    cur.execute("select * from admin")

                    det = cur.fetchone()

                    srf = det[0]
                    base_price = det[1]
                    profit = det[2]

                    cur.execute("select * from profile where username  = ?", (username,))

                    if cur.fetchone()[5] == 'TX':
                        location_factor = 2
                    else:
                        location_factor = 4

                    cur.execute("select count(*) from fuelquote where username  = ?", (username,))

                    if cur.fetchone()[0] > 0:
                        rate_history_factor = 1
                    else:
                        rate_history_factor = 0

                    conn.close()

                    suggested_price = base_price + base_price * (
                            location_factor - rate_history_factor + gallons_requested_factor + profit + srf) / 100

                    # print(gallons_requested_factor, location_factor, rate_history_factor)
                    # print(suggested_price)

                    amount = suggested_price * gallons
                    amount = format(amount, '.2f')

                    return render(request, 'fuel_quote.html',
                                  {'gallons': gallons, 'address': address, 'date': deliveryDate, 'visible': 'visible',
                                   'price': suggested_price, 'amount': amount})
                else:
                    message = 'Delivery Date must be in the future'
                    return render(request, 'fuel_quote.html',
                                  {'message': message, 'gallons': gallons, 'address': address, 'date': deliveryDate,
                                   'visible': 'hidden'})
            else:
                message = 'Address field cannot be empty'
                return render(request, 'fuel_quote.html',
                              {'message': message, 'gallons': gallons, 'address': address, 'date': deliveryDate})
        except ValueError:
            message = 'Gallons must be an integer'
            return render(request, 'fuel_quote.html',
                          {'message': message, 'gallons': gallons, 'address': address, 'date': deliveryDate,
                           'visible': 'hidden'})

    if request.POST.get("submit"):

        if not check_login(request):
            return HttpResponseRedirect('login')

        data = request.POST.copy()

        gallons = data.get("gallons")
        address = data.get("address")
        deliveryDate = data.get("date")
        base = data.get("in1")
        amount = data.get("in2")

        base = base.split(" ")[1]
        amount = amount.split(" ")[1]

        conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')

        cur = conn.cursor()

        username = request.COOKIES['username']

        cur.execute("insert into fuelquote values(?,?,?,?,?,?)",
                    (username, gallons, address, deliveryDate, base, amount))

        conn.commit()

        conn.close()

        return HttpResponseRedirect('fuel_hist')

    else:
        if check_login(request):

            username = request.COOKIES['username']

            conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
            cur = conn.cursor()

            cur.execute("select * from profile")

            addr = ""

            for profile in cur.fetchall():
                if profile[0] == username:
                    addr = profile[2] + ", " + profile[3] + ", " + profile[4] + ", " + profile[5] + " - " + profile[6]

            return render(request, 'fuel_quote.html', {'visible': 'hidden', 'address': addr})
        else:
            return HttpResponseRedirect('login')


def fuel_hist(request):
    if not check_login(request):
        return HttpResponseRedirect('login')

    username = request.COOKIES['username']

    conn = sqlite3.connect(r'/Users/praneethpragada/PycharmProjects/software_design/fuel.db')
    cur = conn.cursor()

    cur.execute("select * from fuelquote where username = ?", (username,))

    rows = []

    for fuelquote in cur.fetchall():
        row = [fuelquote[1], fuelquote[2], fuelquote[3], fuelquote[4], fuelquote[5]]
        rows.append(row)

    rows.reverse()

    rows = rows[:5]

    return render(request, 'fuel_hist.html', {'rows': rows})


def logout(request):
    response = HttpResponseRedirect('login')
    response.delete_cookie('username')
    response.delete_cookie('password')
    return response
