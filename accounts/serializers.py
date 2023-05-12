from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

from .models import User, UserProfile


class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=45)
    phone = serializers.CharField(max_length=16)
    terms = serializers.BooleanField(default=False)
    # username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            "phone",
            "terms", 
            "email",
            # "username",
            "password",
        ]

    def validate(self, attrs):
        terms_false = attrs.get("terms") == False

        if terms_false:
            raise ValidationError("You must agree to the terms before you can continue")

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email already exists")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"



class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["old_password", "new_password"]

    """
    Serializer for password change endpoint.
    """
