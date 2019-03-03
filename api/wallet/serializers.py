from rest_framework.serializers import ModelSerializer, CharField

from expense_manager.models import Wallet


class WalletSerializer(ModelSerializer):
    category = CharField(source='get_category_display')

    class Meta:
        model = Wallet
        fields = ('id', 'name', 'balance', 'category',)
        extra_kwargs = {'id': {'read_only': True}}
