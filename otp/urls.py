# otp/urls.py
from django.urls import path
from .views import SendOTPView,index

urlpatterns = [
    path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    path('',index)
]
