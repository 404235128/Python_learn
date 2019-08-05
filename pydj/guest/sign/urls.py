"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from sign import views_if,views_if_sec,views_if_security

urlpatterns = [
    # guest system interface:
    path('add_event/',views_if.add_event,name='add_event'),
    path('add_guest/',views_if.add_guest,name='add_guest'),
    path('get_event_list/',views_if.get_event_list,name='get_event_list'),
    path('get_guest_list/',views_if.get_guest_list,name='get_guest_list'),
    path('user_sign/',views_if.user_sign,name='user_sign'),
    path('sec_get_event_list/',views_if_sec.get_event_list,name='get_event_list'),
    path('sec_add_event/',views_if_security.add_event,name='add_event'),
    path('sec_get_guest_list/',views_if_sec.get_guest_list,name='get_guest_list'),
]
