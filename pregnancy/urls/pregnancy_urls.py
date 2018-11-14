from django.urls import path

from pregnancy.views import pregnancy_controller as controller

pregnancy_pattern = [
    path('get-all-summary-info', controller.get_all_pregnancy_info),
    path('get-summary-info-by-title', controller.get_pregnancy_info_by_title),
]
