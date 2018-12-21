from django.http import JsonResponse
from rest_framework.decorators import api_view

from pregnancy.db_accessor.db_helper import call_proc
from pregnancy.utils.media_helper import get_media_url


@api_view(['GET'])
def get_all_cooking_info(request):
    db_ret = call_proc(
        'get_all_cooking_info',
        []
    )
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': db_ret
        },
        safe=False
    )


@api_view(['GET'])
def get_cooking_ingredient_by_cooking_id(request):
    cooking_id = request.GET['cookingId']

    db_ret = call_proc(
        'get_cooking_ingredient_by_cooking_id',
        [cooking_id, ]
    )
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': db_ret
        },
        safe=False
    )


@api_view(['GET'])
def get_cooking_step_by_cooking_id(request):
    cooking_id = request.GET['cookingId']

    db_ret = call_proc(
        'get_cooking_step_by_cooking_id',
        [cooking_id, ]
    )
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': db_ret
        },
        safe=False
    )


@api_view(['GET'])
def get_cooking_tip_by_cooking_id(request):
    cooking_id = request.GET['cookingId']

    db_ret = call_proc(
        'get_cooking_tip_by_cooking_id',
        [cooking_id, ]
    )
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': db_ret
        },
        safe=False
    )


@api_view(['GET'])
def get_food_images(request):
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': [
                get_media_url('foods/food_1.jpg'),
                get_media_url('foods/food_2.jpg'),
            ]
        },
        safe=False,
    )

