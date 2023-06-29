from django.urls import path
from me.views import index

my_app = 'me'


urlpatterns = [
    path('', index, name='index')
]