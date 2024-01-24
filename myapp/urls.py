from django.urls import path
from .views import counter, clear


urlpatterns = [
    path('', counter, name='counter'),
    path('clear/', clear, name='clear'),
]
