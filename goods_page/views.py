from django.shortcuts import render


# Create your views here.
def goods_page(request):
    return render(request, 'goods_page/index.html')
