from rest_framework.generics import ListAPIView
from expense_manager.models import Wallet
from .serializers import WalletSerializer


class WalletListView(ListAPIView):
    serializer_class = WalletSerializer

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user=user)
