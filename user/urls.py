from django.urls import path
from .views import  SignUpView,validate_username

urlpatterns = [
    # path('', home, name='home'),
    path('', SignUpView.as_view(), name='signup'),
    path('validate_username', validate_username, name='validate_username')
]