"""nationalpark URL Configuration

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
from django.contrib import admin
from django.urls import path
import park.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results/', park.views.results, name ='results'),
    path('search/', park.views.search, name='search'),
    path('', park.views.index, name='index'),
    path('results/detail/', park.views.detail, name='detail'),
    path('test/', park.views.test, name='test'),
]
