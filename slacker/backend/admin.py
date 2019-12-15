from django.contrib import admin
from .models import Room, RoomType, BeddingConfiguration, RoomNote, Guest, DocumentType, Accommodation, Booking, BookingSource, Payment


admin.site.site_header = "Администрирование ИС Мартон"
admin.site.site_title = "Администрирование ИС Мартон"

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(BeddingConfiguration)
class BeddingConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'daily_price', 'hourly_price', 'bedding_configuration', 'room_type']
    list_filter = ('status', 'room_type', 'bedding_configuration') 
    search_fields = ['name']

@admin.register(RoomNote)
class RoomNoteAdmin(admin.ModelAdmin):
    list_display = ['room', 'created_at', 'created_by', 'content']
    search_fields = ['room__name', 'created_at', 'created_by__username', 'content']

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['id','fullname', 'phone', 'first_visit', 'last_visit']
    search_fields = ['id', 'last_name', 'phone', 'document_number']

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['id', 'check_in', 'check_out', 'room', 'cost']
    list_filter = ['room'] 
    search_fields = ['guests']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'source', 'status', 'check_in', 'check_out']
    list_filter = ['source', 'status', 'room_type'] 
    search_fields = ['guest_name']

@admin.register(BookingSource)
class BookingSourceAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id','payment_type', 'accommodation', 'amount', 'made_on']
    list_filter = ['payment_type', 'made_on'] 
    search_fields = ['id', 'accommodation']



