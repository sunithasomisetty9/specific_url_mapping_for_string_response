from django.urls import path
from app1.views import *


app_name='hi'
urlpatterns=[
    path('prabhas/',prabhas,name='prabhas'),

]