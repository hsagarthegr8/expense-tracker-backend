from django.urls import path

from .views import AccountListView, AccountCreateView

urlpatterns = [
    path('', AccountListView.as_view()),
    path('new/', AccountCreateView.as_view()),
]