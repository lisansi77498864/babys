from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import *

def commodityView(request):
    title = '商品列表'
    classContent = 'commoditys'
    # 根据模型Types 生产商品分类列表
    firsts = Types.objects.values('firsts').distinct()
    typeList = Types.objects.all()
    # 获取请求参数
    t = request.GET.get('t', '')
    s = request.GET.get('s', 'sold')
    p = request.GET.get('p', 1)
    n = request.GET.get('n', '')

    # 根据请求参数查询商品信息
    commodityInfos = CommodityInfos.objects.all()
    if t:
        types = Types.objects.filter(id=t).first()
        commodityInfos = commodityInfos.filter(types=types.seconds)
    if s:
        commodityInfos = commodityInfos.order_by('-'+s)
    if n:
        commodityInfos = commodityInfos.filter(name__contains=n)

    # 分页功能
    paginator = Paginator(commodityInfos, 6)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'commodity.html', locals())
