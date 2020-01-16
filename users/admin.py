from django.contrib import admin
from .models import Profile, UserStripe, Address


admin.site.register(Profile)
admin.site.register(UserStripe)

admin.site.register(Address)