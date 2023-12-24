from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Style, StyleGoods, Goods
import logging
from logger import setLogOptions
from django.db.models import Sum
from django.db.models.functions import Coalesce
from plot.visualize import *
from plot.utils import *


setLogOptions()
logger = logging.getLogger(__name__)


@api_view(['GET'])
def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def chart(request):
    category = request.GET.get('category', '스포티')
    return Response({'filename_img': visualize(category)})


def visualize(category):
    plot, utils = Plot(), Utils()
    return plot.pie(utils.get_data_for_pie(category, category_brand_count()))


def category_brand_count():
    """
    스타일 선택 (ex . 아메카지)
    모든 브랜드 개수 확인
    """
    category_count_data = []
    for category in Style.objects.values('category').distinct():  # 이걸 저 위에 카테고리 하드 코딩된 곳에도 적용하는 게 맞지 않?
        category_name = category['category']
        goods_ids = StyleGoods.objects.filter(style__category=category_name).values_list('goods_id', flat=True)
        brand_count = Goods.objects.filter(id__in=goods_ids).values('brand').annotate(total=Count('brand'))
        category_count_data.append({
            'category': category_name,
            'brand_counts': list(brand_count)
        })

    return {
        'category_brand_counts': category_count_data
    }