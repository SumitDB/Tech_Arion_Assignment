from django.contrib import admin
from .models import Profile,User


# Register your models here.
@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display=("Name", "Date_of_birth","Gender","Phone_number")


@admin.register(User)
class User(admin.ModelAdmin):
    list_display=("owner", "address1","address2","pincode") 