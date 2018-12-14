from django.urls import path

from pregnancy.views import summary_info_controller as si_controller
from pregnancy.views import cooking_controller as c_controller

pregnancy_pattern = [
    path('get-user-log-in', si_controller.get_user_log_in),
    path('get-user-sign-up', si_controller.get_user_sign_up),
    path('get-all-summary-info', si_controller.get_all_summary_info),
    path('get-baby-info-by-week', si_controller.get_baby_info_by_week),
    path('get-mom-info-by-week', si_controller.get_mom_info_by_week),
    path('get-symptom-by-week', si_controller.get_symptom_by_week),
    path('get-advice-by-week', si_controller.get_advice_by_week),
    path('get-all-glossary', si_controller.get_all_glossary),

    path('get-all-cooking-info', c_controller.get_all_cooking_info),
    path('get-cooking-ingredient-by-cooking-id', c_controller.get_cooking_ingredient_by_cooking_id),
    path('get-cooking-step-by-cooking-id', c_controller.get_cooking_step_by_cooking_id),
    path('get-cooking-tip-by-cooking-id', c_controller.get_cooking_tip_by_cooking_id),
]
