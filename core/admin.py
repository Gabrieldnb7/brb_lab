from django.contrib import admin
from checkin.models import CheckIn
from event.models import Event
from subscription.models import Subscription
from users.models import CustomUser

@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'timestamp')
    search_fields = ('user__username', 'event__title')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_time')
    search_fields = ('title',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status')
    search_fields = ('user__username',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
