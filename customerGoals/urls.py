from django.urls import path
from customerGoals import views as customerViews

urlpatterns = [
    path('', customerViews.apiOverview, name='api-overview'),
    path('add-plan/', customerViews.goalCreate, name='add-plan-to-user'),
]