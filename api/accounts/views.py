from rest_framework.generics import ListAPIView

from .serializers import AccountSerializer, User


class AccountListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

