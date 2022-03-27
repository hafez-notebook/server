from django.urls import path
from .views import deleteUserView, signupView, loginView, checkTokenView, goOffline

urlpatterns = [
    path('signup/', signupView.as_view(), name="signupView"),
    path('login/', loginView.as_view(), name="loginView"),
    path('checkToken/', checkTokenView.as_view(), name="checkTokenView"),
    path('delete/', deleteUserView.as_view(), name="deleteUserView"),
    path('goOffline/', goOffline.as_view(), name="goOfflineView"),
]
