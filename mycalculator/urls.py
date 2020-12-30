from django.urls import path
from . import views

urlpatterns=[
    path('',views.cindex, name='cindex'),
    path('calsubmit',views.calsubmit, name='calsubmit'),
]