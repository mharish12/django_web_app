from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('',views.home,name='home'),
    url('predictValue',views.predictValue,name='PredictValue'),
]