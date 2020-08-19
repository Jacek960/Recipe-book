from django.urls import path
from .views import SignUpView, UserUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user_update_profile/', UserUpdate.as_view(), name='user-update-profile'),
]
