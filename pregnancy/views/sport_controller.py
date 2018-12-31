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
        row['benefit'] = SERVER_ENDPOINT + "/static/sports/benefit/" + row['benefit']
        row['step'] = SERVER_ENDPOINT + "/static/sports/step/" + row['step']
        row['note'] = SERVER_ENDPOINT + "/static/sports/note/" + row['note']
    return JsonResponse(
        {
            'err': 0,
            'msg': '',
            'dt': db_ret
        },
        safe=False
    )

