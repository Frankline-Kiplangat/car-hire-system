from django.urls import re_path as url,include
# from django.conf.urls import re_path
from home.views import *
from owner_portal import *
from client_portal import *

urlpatterns = [
    url(r'^$',home),
]
