from rest_framework.serializers import ModelSerializer

from accounts.models import User


class AccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
