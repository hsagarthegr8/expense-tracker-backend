from rest_framework.serializers import ModelSerializer, CharField

from expense_manager.models import Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'name', 'balance', 'category',)
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        user = self.context.get('request').user
        wallet = Wallet(user=user, **validated_data)
        wallet.save()
        return wallet


