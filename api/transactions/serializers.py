from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from expense_manager.models import Transaction


class TransactionSerializer(ModelSerializer):
    type = CharField(source='get_type_display')
    wallet = SerializerMethodField()

    def get_wallet(self, obj):
        return obj.wallet.name

    class Meta:
        model = Transaction
        exclude = ('user',)
