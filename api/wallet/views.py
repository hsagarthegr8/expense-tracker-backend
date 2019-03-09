from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from expense_manager.models import Wallet
from .serializers import WalletSerializer


class WalletListView(ListAPIView):
    serializer_class = WalletSerializer

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)


class WalletCreateView(CreateAPIView):
    serializer_class = WalletSerializer


class WalletUpdateView(UpdateAPIView):
    serializer_class = WalletSerializer

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)
