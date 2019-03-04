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


