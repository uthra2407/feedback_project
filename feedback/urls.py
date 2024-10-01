from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.submit_feedback, name='submit_feedback'),
    path('success/', views.feedback_success, name='feedback_success'),
]
