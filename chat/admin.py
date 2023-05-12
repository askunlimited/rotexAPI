from django.contrib import admin

from .models import Conversations


@admin.register(Conversations)
class ConversationsAdmin(admin.ModelAdmin):
    list_display = ["product", "name", "subject", "email", "telephone", "created_on"]
    list_filter = ["created_on"]

