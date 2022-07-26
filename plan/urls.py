from django.urls import path
from plan import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('plan-list/', views.planList, name='plan-list'),
    path('plan-create/', views.planCreate, name='plan-create'),
    path('plan-update/<int:pk>/', views.planUpdate),
]