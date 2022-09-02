import imp
from django.urls import path
from xam_xam.views import index

urlpatterns = [
    path('',index,name='home'),
]
