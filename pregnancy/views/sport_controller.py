from django.http import JsonResponse
from rest_framework.decorators import api_view

from configs.settings import SERVER_ENDPOINT
from pregnancy.db_accessor.db_helper import call_proc


@api_view(['GET'])
def get_all_sport_info(request):
    db_ret = call_proc(
        'get_all_sport_info',
        []
    )

    for row in db_ret:
        row['picture'] = SERVER_ENDPOINT+"/static/sports/picture/"+row['picture']
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': db_ret
        },
        safe=False
    )
