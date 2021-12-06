from django.urls import path
from .views import deleteUserView, signupView, loginView, checkTokenView

urlpatterns = [
    path('login/', loginView.as_view(), name="loginView"),
    path('checkToken/', checkTokenView.as_view(), name="checkTokenView"),
    path('delete/', deleteUserView.as_view(), name="deleteUserView"),
]