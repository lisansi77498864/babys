from django.urls import path
from .views import *

urlpatterns = [
    path('.html', commodityView, {'user': 'admin'}, name='commodity'),
    #path('/detail.<int:id>.html', detailView, name='detail'),
]