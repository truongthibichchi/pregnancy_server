from django.urls import path

from pregnancy.views import pregnancy_controller as controller

pregnancy_pattern = [
    path('get-user-log-in', controller.get_user_log_in),
    path('get-user-sign-up', controller.get_user_sign_up),
    path('get-all-summary-info', controller.get_all_summary_info),
    path('get-baby-info-by-week', controller.get_baby_info_by_week),
    path('get-mom-info-by-week', controller.get_mom_info_by_week),
    path('get-symptom-by-week', controller.get_symptom_by_week),
    path('get-advice-by-week', controller.get_advice_by_week),

]
