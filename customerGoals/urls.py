from django.urls import path

from plan import views as planViews
from customerGoals import views as customerViews

urlpatterns = [
    path('', customerViews.apiOverview),
    path('add-plan/', customerViews.goalCreate),
]