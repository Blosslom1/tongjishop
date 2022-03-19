from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def user_main_page(request):
    return render(request, "user_page/index.html")


def portfolio(request):
    return render(request, 'user_page/portfolio.html')


def testimonials(request):
    return render(request, "user_page/testimonials.html")
