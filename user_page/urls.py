from django.urls import path
from . import views

urlpatterns = [
    path('user_info', views.user_main_page),
    # 页面的另几个板块
    path('portfolio', views.portfolio),
    path('testimonials', views.testimonials)

]
