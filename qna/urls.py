from django.urls import path
from . import views
from qna import views

urlpatterns=[
    path('',views.home,name='home'),
    path('sheet',views.sheet,name='sheet'),
    path('result',views.result, name='result'),


]