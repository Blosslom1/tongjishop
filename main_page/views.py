from django.shortcuts import render


# Create your views here.
# 网站首页
def MainPage(request):
    dic1 = {"page": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}
    return render(request, 'main_page/index.html', locals())
