from django.http import JsonResponse
from rest_framework.decorators import api_view

from pregnancy.db_accessor.db_helper import call_proc


@api_view(['GET'])
def get_all_summary_info(request):
    db_ret = call_proc(
        'get_all_summary_info',
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
def get_baby_info_by_week(request):
    week = request.GET['week']

    db_ret = call_proc(
        'get_baby_info_by_week',
        [week, ]
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
def get_mom_info_by_week(request):
    week = request.GET['week']

    db_ret = call_proc(
        'get_mom_info_by_week',
        [week, ]
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
def get_symptom_by_week(request):
    week = request.GET['week']

    db_ret = call_proc(
        'get_symptom_by_week',
        [week, ]
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
def get_advice_by_week(request):
    week = request.GET['week']

    db_ret = call_proc(
        'get_advice_by_week',
        [week, ]
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
def get_user_log_in(request):
    err = 0
    msg = 'Login successfully'

    email = request.GET['email']
    password = request.GET['password']

    db_ret = call_proc(
        'get_user_log_in',
        [email, password]
    )
    if db_ret is None:
        err = 1
        msg = 'Wrong username or password'
        db_ret = ''
    else:
        db_ret = db_ret[0]

    return JsonResponse(
        {
            'err': err,
            'msg': msg,
            'dt': db_ret,
        },
        safe=False
    )

@api_view(['GET'])
def get_user_sign_up(request):
    err = 0
    msg = 'Sign up successfully'

    email = request.GET['email']
    password = request.GET['password']
    fullname = request.GET['fullname']
    conceivedDate = request.GET['conceivedDate']

    db_ret = call_proc(
        'get_user_sign_up',
        [email, password, fullname, conceivedDate]
    )
    if db_ret is None:
        err = 1
        msg = 'Sign up failed'
        db_ret = ''
    else:
        db_ret = db_ret[0]

    return JsonResponse(
        {
            'err': err,
            'msg': msg,
            'dt': db_ret,
        },
        safe=False
    )

