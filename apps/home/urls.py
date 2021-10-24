# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # The home page v2
    path('v2', views.index_v2, name='home_v2'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
