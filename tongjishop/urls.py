"""tongjishop URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Mainpage路由路径
    path('', include('main_page.urls')),
    # 用户页面路由
    path('userpage/', include('user_page.urls')),
    # 商品展示页路由
    path('goodspage/', include('goods_page.urls')),

    path('bio_consume/', views.bio_consume),
    path('exp_instruction/', views.exp_instruction),
]
