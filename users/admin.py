from django.contrib import admin
from users.models import UserDB, UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ("name", "id", "user")
    list_display = ("id", "name", "user")


admin.site.register(UserDB)
admin.site.register(UserProfile, UserProfileAdmin)

