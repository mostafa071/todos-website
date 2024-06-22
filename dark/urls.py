"""
URL configuration for dark project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from core.views import PostDetailView,PostListView
from django.views.generic import RedirectView
from theme.views import change_theme

from todos.views import add_todo, index , update_todo, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path(" " , index , name="index"),
    path("add-todo/" , add_todo , name="add-todo"),
    path("update-todo/<int:pk>" , update_todo , name="update_todo"),
    path("delete/<int:pk>" , delete , name="delete"),
    path('switch-theme' ,  change_theme, name="change-theme"),
    path('' ,  PostListView.as_view(), name="main"),
    path('<pk>/' ,  PostDetailView.as_view(), name="detail"),
]

