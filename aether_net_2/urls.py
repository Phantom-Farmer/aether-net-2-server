from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from aethernetapi.views import register_user, check_user
from aethernetapi.views import UserView, SleepCardView, DreamJournalView, TagView, SCTagView
"""aether_net_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'users')
router.register(r'sleep_card', SleepCardView, 'sleep_card')
router.register(r'dream_journal', DreamJournalView, 'dream_journal')
router.register(r'tag', TagView, 'tag')
router.register(r'sc_tag', SCTagView, 'sc_tag')


urlpatterns = [
# Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
# Requests to http://localhost:8000/checkuser will be routed to the login_user function
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
