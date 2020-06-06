from django.contrib import admin
from front.models import Hotel, Reservation, Gallery

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
