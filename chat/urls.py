from django.urls import path

from .views import ConversationView, ListConversationsView, ConversationsRetrieveUpdateDeleteView

urlpatterns = [
    path("", ListConversationsView.as_view(), name="list_messages"),

    path("add/", ConversationView.as_view(), name='create_message'),

    path("<int:pk>/", ConversationsRetrieveUpdateDeleteView.as_view(), name="message_detail")

]