"""django2_basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.http import HttpResponse
from .views import *
from django.conf import settings

def mysum(request, x, y):
    result = x + y
    return HttpResponse('result={}'.format(result))

urlpatterns = [
    path('rhksflwk/', admin.site.urls),
    path('mysum/<int:x>/<int:y>/', mysum),
    path('shop/', include("shop.urls")),
    path('csv/', response_csv),
    path('excel/', response_excel),
    path('image/', response_pillow),
    path('blog/', include("blog.urls"))
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]