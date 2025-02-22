"""Capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('mainapp.urls'), name="home"),
    path('practice/', include('practiceapp.urls')),
    path('upractice/', include('upracticeapp.urls')),
    path('board/', include('boardapp.urls')),
    path('post/', include('postapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('game/', include('gameapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'mainapp.views.page_not_found'