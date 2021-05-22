"""albaproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from albaapp.views import home, detail, create_page, create, update_page, update, delete, plus, minus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('detail/<int:id>/', detail, name='detail'),
    path('create_page/', create_page, name='create_page'),
    path('create', create, name='create'),
    path('update_page/<int:id>/', update_page, name='update_page'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('plus/<int:id>/', plus, name='plus'),
    path('minus/<int:id>/', minus, name='minus'),
]
 