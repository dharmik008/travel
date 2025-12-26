from http.cookiejar import deepvalues

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template.defaultfilters import dictsort
from requests.utils import dict_from_cookiejar
from traveler.models import *
# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff == True:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, "Not an admin user.")
            return redirect('/admin_login/')

    return render(request, 'admin_login.html')

def admin_dashboard(request):
    # db = dashboard.objects.all()
    return render(request,'dashboard.html')

def hotel_book_a(request):
    # hb = hotel_book_a.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        guests = request.POST['guests']
        price = request.POST['price']
        total_price = request.POST['total_price']
        message = request.POST['message']
        is_booking = request.POST['is_booking']
        payment_status = request.POST['payment_status']

        hc = Hotel_booking.objects.create(name=name,email=email,checkin=checkin,checkout=checkout,total_price=total_price,guests=guests,price=price,message=message,is_booking=is_booking,payment_status=payment_status)
        return redirect('/hotel_book_a')
    return render(request,'hotel_book_a.html',)

def hotel_book_a_read(request):
    br = Hotel_booking  .object.all()
    return render(request, 'hotel_book_a_read')

def hotel_book_a_update(request):
    hu = hotel_book_a.objects.get(id=id)
    db = dashboard.objects.all()

    if request.methid=="POST":
        name = request.POST['name']
        email = request.POST['email']
        checkin = request.POST['checkin']
        guests = request.POST['guests']
        price = request.POST['price']
        message = request.POST['message']
        is_booking = request.POST['is_booking']
        payment_status = request.POST['payment_status']

        hu.name=name
        hu.email=email
        hu.checkin=checkin
        hu.guests=guests
        hu.price=price
        hu.message=message
        hu.is_booking=is_booking
        hu.payment_status=payment_status
        return redirect("/dashboard")
    return render(request,"hotel_book_a_update")

def add_hotel(request):
    dc = None

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        price = request.POST['price']
        rating = request.POST['rating']
        location = request.POST['location']
        dc = Hotel.objects.create(name=name,description=description,image=image,price=price,rating=rating,location=location)
        return redirect('/add_hotel')
    return render(request, 'add_hotel.html', {'dc': dc})

def add_hotel_update(request):
    au = add_hotel.objects.get(id=id)
    db= dashboard.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        price = request.POST['price']
        rating = request.POST['rating']
        location = request.POST['location']

        au.name = name
        au.description = description
        au.image = image
        au.price = price
        au.rating = rating
        au.location = location

        return redirect("/dashboard")
    return render(request,"add_hotel_update.html",{'au':au ,'db':db})

def tour_book_a(request):
    if request.method == "POST":
        username = request.POST['username']
        tour_id = request.POST['tour_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        destination = request.POST['destination']
        no_person = request.POST['no_person']
        price = request.POST['price']
        total_price = request.POST['total_price']
        duration = request.POST['duration']
        is_booking = request.POST['is_booking']

        tc = Tour_booking.objects.create(username=username, tour_id=tour_id,first_name=first_name,last_name=last_name,phone=phone,email=email,destination=destination,no_person=no_person,price=price, total_price=total_price,duration=duration,is_booking=is_booking)

        return redirect('/tour_book_a')
    return render(request, 'tour_book_a.html')

def tour_book_a_read(request):
    br = Tour_booking.object.all()
    return render(request, 'tour_book_a_read')

def tout_book_a_update(request):
    bu = tour_book_a.objects.get(id=id)
    db = dashboard.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        tour_id = request.POST['tour_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        destination = request.POST['destination']
        no_person = request.POST['no_person']
        price = request.POST['price']
        total_price = request.POST['total_price']
        duration = request.POST['duration']
        is_booking = request.POST['is_booking']

        bu.username=username
        bu.tour_id=tour_id
        bu.first_name=first_name
        bu.last_name=last_name
        bu.phone=phone
        bu.email=email
        bu.destination=destination
        bu.no_person=no_person
        bu.price=price
        bu.total_price=total_price
        bu.duration=duration
        bu.is_booking=is_booking
        return redirect("/dashboard")
    return render(request,"tour_book_a_update.html",{'bu':bu,'db':db})


def tour_admin(request):
    if request.method == "POST":
        category_name = request.POST['category_name']
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        price = request.POST['price']
        rating = request.POST['rating']
        duration = request.POST['duration']
        location = request.POST['location']

        # Use correct field name: Cat_name (capital C)
        try:
            category = Tour_cat.objects.get(Cat_name=category_name)
        except Tour_cat.DoesNotExist:
            messages.error(request, "Category not found.")
            return redirect('/tour_admin')

        Tour.objects.create(
            Category_name=category,  # assuming model uses capital C
            name=name,
            description=description,
            image=image,
            price=price,
            rating=rating,
            duration=duration,
            location=location
        )

        return redirect('/tour_admin')

    categories = Tour_cat.objects.all()
    return render(request, 'tour_Admin.html', {'categories': categories})


def tour_admin_update(request):
    ou = tour_admin.objects.get(id=id)
    db = dashboard.objects.all()

    if request.method == "POST":
        Category_name = request.POST['Category_name']
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILE['image']
        price = request.POST['price']
        rating = request.POST['rating']
        duration = request.POST['duration']
        location = request.POST['location']

        ou.Category_name = Category_name
        ou.name = name
        ou.description = description
        ou.image = image
        ou.price = price
        ou.rating = rating
        ou.duration = duration
        ou.location = location

        return redirect("/dashboard")
    return render(request,"tour_admin_update",{'ou':ou,'db':db})

def tour_cat_a(request):
    # ct = tour_cat_a.objects.all()
    if request.method == "POST":
        cat_name=request.POST['cat_name']
        cc = Tour_cat.objects.create(cat_name=cat_name)
        return redirect('/toru_cat_a')
    return render(request, 'tour_cat_a.html',)

def tour_cat_a_update(request):
    cu = tour_cat_a_update.objects.get(id=id)
    db = dashboard.objects.all()

    if request.method == "POST":
        cat_name = request.POST['cat_name']

        cu.cat_name=cat_name

        return redirect("/dashboard")
    return render(request,'tour_cat_a_update',{'cu':cu , 'db':db})