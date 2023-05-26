from django.urls import path
from app2.views import *

app_name='hello'

urlpatterns=[
    path('prabhas/',prabhas,name='prabhas'),
]


