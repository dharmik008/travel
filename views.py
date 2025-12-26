
import razorpay
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def home(request):
    h = Tour.objects.all()
    for rating in h:
        rating.full_stars = range(rating.rating)
        rating.empty_stars = range(5 - rating.rating)

    if request.GET.get('search'):
        s = request.GET.get('search')
        h = Tour.objects.filter(location__icontains=s)
    return render(request,'home.html',{'h':h})

def about(request):
    return render(request,'about.html')

def tour(request):
    t = Tour.objects.all()
    for rating in t:
        rating.full_stars = range(rating.rating)
        rating.empty_stars = range(5 - rating.rating)
    if request.GET.get('search'):
        s = request.GET.get('search')
        t = Tour.objects.filter(location__icontains=s)
    return render(request, 'tour.html',{'t':t})

# def destination(request):
#     destinations = Destination.objects.all()
#     return render(request, 'tour_a.html',{'cat': destinations})

def hotel(request):
    h = Hotel.objects.all()
    for rating in h:
        rating.full_stars = range(rating.rating)
        rating.empty_stars = range(rating.rating)
    return render(request,'hotel.html',{'h':h})

def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        c = Contact.create(name=name,email=email,subject=subject,message=message)
        return redirect('contact')
    return render(request,'contact.html')

# def home(request):
#     return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(username=username):
        #     return redirect('/')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.f_name = f_name
        myuser.l_name = l_name

        myuser.save()

        # messages.success(request, "Your Account is created")

        return redirect('/signin')

    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # f_name = user.first_name
            # return render(request,'home.html', {'f_name': f_name})
            return redirect('/')
        else:
            messages.error(request, "not user")
            return redirect('/signin')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "you have logout")
    return redirect('/')

def information(request,id):
    o = Tour.objects.get(id=id)
    return render(request,'information.html',{'o':o})

def hotel_info(request,id):
    o2 = Hotel.objects.get(id=id)
    return render(request,'hotel_info.html',{'o2':o2})

def tour_booking(request,id):
    tb = Tour.objects.get(id=id)
    user = request.user

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        phone = request.POST['phone']
        email = request.POST['email']
        destination = request.POST['destination']
        no_person = int(request.POST['no_person'])
        price = int(request.POST['price'])
        duration = request.POST['duration']
        t_price = request.POST['t_price']
        total_price = no_person * price

        # Initialize Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Create Razorpay Order
        amount_in_paise = total_price * 100  # Convert to paise
        razorpay_order = client.order.create({
            'amount': amount_in_paise,
            'currency': 'INR',
            'payment_capture': 1
        })

        # Save booking with Razorpay Order ID
        b = Tour_booking.objects.create(
            username=user,
            Tour_id=tb,
            f_name=f_name,
            l_name=l_name,
            phone=phone,
            email=email,
            destination=destination,
            price=price,
            duration=duration,
            is_booking=True,
            no_person=no_person,
            t_price=total_price,
            razorpay_order_id=razorpay_order['id'],
            payment_status="Complete"
        )

        return render(request, "tour_booking.html", {
            'tb': tb,
            'razorpay_key': settings.RAZORPAY_KEY_ID,
            'razorpay_order_id': razorpay_order['id'],
            'currency': "INR",
            't_price': t_price
        })

    return render(request, "tour_booking.html", {'tb': tb})

def hotel_booking(request,id):
    hb = Hotel.objects.get(id=id)
    user = request.user

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        no_guest = int(request.POST['no_guests'])
        price = int(request.POST['price'])
        message = request.POST['message']

        total_price = no_guest * price

        # Initialize Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Create Razorpay Order
        amount_in_paise = total_price * 100  # Convert to paise
        razorpay_order = client.order.create({
            'amount': amount_in_paise,
            'currency': 'INR',
            'payment_capture': 1
        })

        b1 = Hotel_booking.objects.create(
            user=user,
            name = name,
            email = email,
            checkin = checkin,
            checkout = checkout,
            no_guest = no_guest,
            price = price,
            message = message,
            is_booking = True,
            total_price = total_price,
            razorpay_order_id=razorpay_order['id'],
            payment_status="Complete"
        )

        return render(request, "hotel_booking.html",{
            'hb':hb,
            'razorpay_key': settings.RAZORPAY_KEY_ID,
            'razorpay_order_id': razorpay_order['id'],
            'currency': "INR",
            'total_price': total_price
        })

    return render(request,'hotel_booking.html',{'hb':hb})

# def history(request):
#     hb = Hotel_booking.objects.all()
#     tb = Tour_booking.objects.all()
#
#     return render(request, 'history.html',{
#         'hb': hotel_booking,
#         'tb': tour_booking,
#     })

def history(request):
    h=Tour_booking.objects.filter(username=request.user)
    b=Hotel_booking.objects.filter(user=request.user)
    context={
        'h':h,
        'b':b
    }
    return render(request,"history.html",context)