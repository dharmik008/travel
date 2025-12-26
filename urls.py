
from django.urls import path
from . import views

urlpatterns = ([
    path('',views.home),
    path('about/',views.about),
    path('tour/',views.tour),
    path('hotel/',views.hotel),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('tour_booking/<int:id>/',views.tour_booking),
    path('hotel_booking/<int:id>/',views.hotel_booking),
    path('information/<int:id>/',views.information),
    path('hotel_info/<int:id>/',views.hotel_info),
    path('history/',views.history),

])