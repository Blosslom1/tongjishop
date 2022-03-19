# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    # Mainpage路由路径
    path('', views.MainPage),
]
# urlpatterns += staticfiles_urlpatterns()
