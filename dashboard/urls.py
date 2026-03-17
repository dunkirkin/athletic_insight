from django.urls import path
from .views import dashboard_view, activity_summary_view, training_load_view, wellness_stress_view, sleep_score_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('activity_summary.html', activity_summary_view, name="activity_summary"),
    path('training_load.html', training_load_view, name='training_load'),
    path('wellness_stress.html', wellness_stress_view, name='wellness_stress'),
    path('sleep_score.html', sleep_score_view, name='sleep_score')
]