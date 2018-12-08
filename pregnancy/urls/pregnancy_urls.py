from django.urls import path

from pregnancy.views import pregnancy_controller as controller

pregnancy_pattern = [
    path('get-user-log-in', controller.get_user_log_in),
    path('get-user-sign-up', controller.get_user_sign_up),
    path('get-all-summary-info', controller.get_all_summary_info),
    path('get-summary-info-by-week', controller.get_pregnancy_info_by_week),
]
