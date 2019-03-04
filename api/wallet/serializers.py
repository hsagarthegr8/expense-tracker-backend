from rest_framework.serializers import ModelSerializer, CharField

from expense_manager.models import Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'user', 'name', 'balance', 'category',)
        extra_kwargs = {'id': {'read_only': True}, 'user': {'write_only': True}}
