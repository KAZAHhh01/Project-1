from django.contrib import admin

from Good_Trip.models import Location, Event, Ticket, Hotel

admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Hotel)