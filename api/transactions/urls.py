from django.urls import path
from .views import TransactionListView, TransactionCreateView, TransactionDeleteView, TransactionUpdateView

urlpatterns = [
    path('', TransactionListView.as_view()),
    path('new/', TransactionCreateView.as_view()),
    path('<int:pk>/delete/', TransactionDeleteView.as_view()),
    path('<int:pk>/update/', TransactionUpdateView.as_view()),
]