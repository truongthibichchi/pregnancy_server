from django.http import JsonResponse
from rest_framework.decorators import api_view

from pregnancy.db_accessor.db_helper import call_proc


@api_view(['GET'])
def get_all_pregnancy_info(request):
    db_ret = call_proc(
        'summary_info_get_all'
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
def get_pregnancy_info_by_title(request):
    title = request.GET['title']

    db_ret = call_proc(
        'summary_info_get_by_title',
        [title, ]
    )
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': db_ret
        },
        safe=False
    )
