from rest_framework.serializers import ModelSerializer
from expense_manager.models import Transaction


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context.get('request').user
        transaction = Transaction(user=user, **validated_data)
        transaction.save()
        return transaction

    def update(self, instance, validated_data):
        amount = validated_data['amount']
        transaction_type = validated_data['type']
        wallet = validated_data['wallet']
        instance.update_wallet_balance_wrt_new_amount(transaction_type=transaction_type, amount=amount, wallet=wallet)
        return super().update(instance, validated_data)

