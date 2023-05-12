from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics, mixins, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)

from .serializers import ConversationSerializer

from .models import Conversations


class ConversationView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data['product']
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            telephone = serializer.validated_data['telephone']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            serializer.save()

            message = {
                product: product,
                name: name,
                telephone: telephone,
                message: message
            }

            send_mail(

                subject=subject,
                message={message},
                from_email=email,
                recipient_list=['adikasking@gmail.com'],
            )
            return Response({'message': 'Email sent successfully'})
        return Response(serializer.errors, status=400)


class ListConversationsView(APIView):
    permission_classes = []
    def get(self, request):
        list_conversations = Conversations.objects.all()
        serializer = ConversationSerializer(list_conversations, many=True)
        return Response(serializer.data)



class ConversationsRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Conversations.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
