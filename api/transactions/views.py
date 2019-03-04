from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import TransactionSerializer
from expense_manager.models import Transaction


class TransactionListView(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user).order_by('-date')


class TransactionCreateView(CreateAPIView):
    serializer_class = TransactionSerializer


class TransactionDeleteView(DestroyAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)


class TransactionUpdateView(UpdateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

