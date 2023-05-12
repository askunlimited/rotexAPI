from django.contrib import admin


from .models import Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "slug", "created_on")
    list_filter = ["created_on"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Page, PageAdmin)