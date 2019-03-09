from django.urls import path

from .views import WalletListView, WalletCreateView, WalletUpdateView

urlpatterns = [
    path('', WalletListView.as_view()),
    path('new/', WalletCreateView.as_view()),
    path('<int:pk>/update/', WalletUpdateView().as_view())
]