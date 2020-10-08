from django.urls import path
from .views import *

urlpatterns = [
    path('user', UserView.as_view(), name='user-list-create'),
    path('user/<int:pk>', SingleUserView.as_view(), name='user-update-delete')
]