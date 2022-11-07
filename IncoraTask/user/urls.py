from django.urls import path
from .views import UserListCreateView, UserRetrieveView


urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('<int:id>/', UserRetrieveView.as_view()),
]