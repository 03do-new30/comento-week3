"""drf_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from todos.views import TodoViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from rest_framework_nested import routers


# Create a router and register our viewsets with it.
router = routers.SimpleRouter()
router.register(r'todos', TodoViewSet)
router.register(r'comments', CommentViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = router.urls