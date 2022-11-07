from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

CustomUserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUserModel.objects.create_user(**validated_data)
        user.save()

        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
