from rest_framework.generics import ListAPIView
from .serializers import TransactionSerializer
from expense_manager.models import Transaction


class TransactionListView(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)
