from django.contrib import admin
from django.urls import path,include
from django.urls import path
from . import views
urlpatterns = ([
    path('admin_login/',views.admin_login),
    path('dashboard/',views.admin_dashboard),
    path('hotel_book_a/',views.hotel_book_a),
    path('tour_book_a/',views.tour_book_a),
    path('add_hotel/',views.add_hotel),
    path('tour_admin/', views.tour_admin),
    path('tour_cat_a/',views.tour_cat_a),
])