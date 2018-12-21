from django.http import JsonResponse
from rest_framework.decorators import api_view

from pregnancy.db_accessor.db_helper import call_proc


@api_view(['GET'])
def get_all_sport_info(request):
    db_ret = call_proc(
        'get_all_sport_info',
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
