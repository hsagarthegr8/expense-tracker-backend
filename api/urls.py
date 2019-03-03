from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('accounts/', include('api.accounts.urls')),
    path('wallets/', include('api.wallet.urls')),
    path('transactions/', include('api.transactions.urls')),
    path('get-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('verify-token/', verify_jwt_token),
]