from django.contrib import admin
from .models import Event, Participent

# Register your models here.

class ParticipentAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'institute_name', 'phone')
    search_fields = ('name','institute_name')
    list_filter= ('year', 'institute_name')

    class Meta:
        model = Participent

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_venue', 'regn_fees','event_contact')
    search_fields = ('evnt_name', 'event_description')
    list_filter= ('event_venue',)
    

    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)
admin.site.register(Participent,ParticipentAdmin )
