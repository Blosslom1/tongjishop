from django.http import HttpResponse
from django.shortcuts import render


# 生物医药耗材
def bio_consume(request):
    html = "<h1>这是生物耗材板块<h1>"
    return HttpResponse(html)


# 实验器具板块
def exp_instruction(resquest):
    html = "<h1>这是实验器具板块<h1>"
    return HttpResponse(html)
