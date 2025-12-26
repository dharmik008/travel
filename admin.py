from django.contrib import admin

from traveler.models import Contact, Tour, Hotel

from traveler.models import Tour_cat,Tour_booking,Hotel_booking


# from traveler.models import Information

# Register your models here.
admin.site.register(Contact)
admin.site.register(Tour)
admin.site.register(Hotel)
admin.site.register(Tour_cat)
admin.site.register(Tour_booking)
admin.site.register(Hotel_booking)
# admin.site.register(Information)