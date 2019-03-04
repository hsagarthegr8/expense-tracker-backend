from django.urls import path

from .views import WalletListView, WalletCreateView

urlpatterns = [
    path('', WalletListView.as_view()),
    path('new/', WalletCreateView.as_view()),
]