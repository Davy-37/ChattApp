"""
URL configuration for DBE_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from chat_app import views as chat_views
from chat_app.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_views.landing_page, name='landing_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat_app.urls')),
    path('register/', chat_views.register_view, name='register'),
    path('logout/', custom_logout, name='logout'),
    path('login/', chat_views.login_view, name='login'),
]
