from django.contrib import admin
from .models import UserData, ExpressAddress, AmountMoney, ShoppingCart, GoodsCollection


# Register your models here.
# 用户后台管理
class UserDataManage(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_really_name', 'company_school', 'sex', 'user_portrait']
    list_display_links = ['user_name']
    list_filter = ['company_school', 'sex', 'user_portrait']
    search_fields = ['id', 'user_name', 'user_really_name', 'company_school', 'user_portrait']
    list_editable = ['user_really_name', 'company_school', 'sex', 'user_portrait']


admin.site.register(UserData, UserDataManage)


# 用户快递地址后台管理
class ExpressAddressManage(admin.ModelAdmin):
    list_display = ['id', "user_data", 'country', 'province', 'city', 'area', 'street', 'name', 'phone']
    list_display_links = ['id']
    list_filter = ['country', 'province', 'city', 'area', 'street']
    search_fields = ['id', 'country', 'province', 'city', 'area', 'street', 'name', 'phone']
    list_editable = ['country', 'province', 'city', 'area', 'street', 'name', 'phone']


admin.site.register(ExpressAddress, ExpressAddressManage)


# 用户金额积分后台管理
class AmountMoneyManger(admin.ModelAdmin):
    list_display = ['user_data', 'money', 'consume', 'integral', 'integral_consume']
    list_display_links = ['user_data']
    search_fields = ['user_data', 'money', 'consume', 'integral', 'integral_consume']
    list_editable = ['integral', 'integral_consume']


admin.site.register(AmountMoney, AmountMoneyManger)


# 用户商品收藏后台管理
class GoodsCollectionManager(admin.ModelAdmin):
    list_display = ['user_data', 'goods_name', 'collection_data', 'collection_time']
    list_display_links = ['user_data']
    list_filter = ['goods_name']
    search_fields = ['user_data', 'goods_name', 'collection_data', 'collection_time']


admin.site.register(GoodsCollection, GoodsCollectionManager)


# 用户购物车后台管理
class ShoppingCartManager(admin.ModelAdmin):
    list_display = ['user_data', 'goods_name', 'collection_data', 'collection_time']
    list_display_links = ['user_data']
    list_filter = ['goods_name']
    search_fields = ['user_data', 'goods_name', 'collection_data', 'collection_time']


admin.site.register(ShoppingCart, ShoppingCartManager)
