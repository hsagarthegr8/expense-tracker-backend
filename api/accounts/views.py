from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import AccountSerializer, User


class AccountListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer


class AccountCreateView(CreateAPIView):
    serializer_class = AccountSerializer

