from django.contrib import admin
from .models import User, UserProfile

# Register your models here.

admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
  list_display = ["email", "phone"]
  list_filter = ["email"]


admin.site.register(UserProfile)


class UserProfileAdmin(admin.ModelAdmin):

  list_display = ["first_name", "last_name", "phone"]
  list_filter = ["first_name"]

