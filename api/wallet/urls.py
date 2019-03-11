from django.urls import path

from .views import WalletListView, WalletCreateView, WalletUpdateView, WalletDeleteView

urlpatterns = [
    path('', WalletListView.as_view()),
    path('new/', WalletCreateView.as_view()),
    path('<int:pk>/update/', WalletUpdateView.as_view()),
    path('<int:pk>/delete/', WalletDeleteView.as_view())
]