from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('reports/<int:pk>', views.employee_report, name='report'),
    path('delete_report/<int:pk>', views.delete_report, name='delete_report'),
    path('add_report/', views.add_report, name='add_report'),
    path('update_report/<int:pk>', views.update_report, name='update_report'),
]

