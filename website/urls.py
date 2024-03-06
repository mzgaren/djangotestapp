from django.urls import path
from . import views
from .views import ChartData


urlpatterns = [
    path('report/', views.home, name='report_list'),
    path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    #path('stats/', views.stats, name='statistics'),
    path('api/chart/data', ChartData.as_view()),
    path('register/', views.register_user, name='register'),
    path('reports/<int:pk>', views.employee_report, name='report'),
    path('delete_report/<int:pk>', views.delete_report, name='delete_report'),
    path('add_report/', views.add_report, name='add_report'),
    path('update_report/<int:pk>', views.update_report, name='update_report'),
]

