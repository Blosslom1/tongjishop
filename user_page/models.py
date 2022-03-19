from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
# 用于存放用户信息的数据模型。
class UserData(models.Model):
    # 用户昵称
    user_name = models.CharField("用户昵称", max_length=50, default="")
    # 用户真实姓名
    user_really_name = models.CharField("用户姓名", max_length=10, default="")
    # 公司/学校
    company_school = models.CharField('机构', max_length=50, default="")
    # 用户性别
    sex = models.BooleanField("性别", default="True")
    # 用户头像
    user_portrait = models.ImageField('头像', null=False, default='1.png')
    address = models.CharField("用户地址", max_length=100, default="", null=False)

    class Meta:
        db_table = "userdata"
        verbose_name_plural = '用户信息'


# 收货地址类user对ExpressAddress一对多
class ExpressAddress(models.Model):
    country = models.CharField("国家", max_length=50, null=False, default='中国')
    province = models.CharField("省份", max_length=50, null=False, default='湖南')
    city = models.CharField("市", max_length=10, default="长沙", null=False)
    area = models.CharField('区/县', max_length=10, null=False, default='')
    street = models.CharField('街道/镇', max_length=10, null=False, default='')
    name = models.CharField('姓名', max_length=10, null=False, default='')
    phone = models.CharField('电话', null=False, max_length=11, default=88888888888)
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE, null=False, default='')

    class Meta:
        db_table = "express_address"
        verbose_name_plural = '地址信息'


# 用户支付系统数据库一对一
class AmountMoney(models.Model):
    money = models.DecimalField('金额', max_digits=11, decimal_places=2, default=0)
    consume = models.DecimalField('开销', max_digits=15, decimal_places=2, default=0)
    integral = models.IntegerField('积分', default=0,
                                   validators=[MinValueValidator(1), MaxValueValidator(10000000000000)])
    integral_consume = models.IntegerField('积分开销', default=0,
                                           validators=[MinValueValidator(1), MaxValueValidator(10000000000000000)])
    user_data = models.OneToOneField(UserData, on_delete=models.CASCADE)

    class Meta:
        db_table = 'amount_money'
        verbose_name_plural = '用户金额/积分'


# 用户收藏数据库一对多
class GoodsCollection(models.Model):
    goods_name = models.CharField('商品名', max_length=200, default='', null=False)

    collection_data = models.DateField('收藏日期', auto_now_add=True, )
    collection_time = models.DateTimeField('收藏时间', auto_now_add=True)
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)

    class Meta:
        db_table = 'goods_collection'
        verbose_name_plural = '用户收藏'


# 用户购物车数据库一对多
class ShoppingCart(models.Model):
    goods_name = models.CharField('商品名', max_length=200, default='', null=False)

    collection_data = models.DateField('加入日期', auto_now_add=True, )
    collection_time = models.DateTimeField('加入时间', auto_now_add=True)
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)

    class Meta:
        db_table = "shopping_cart"
        verbose_name_plural = '用户购物车'
