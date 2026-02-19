from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('submit/', views.submit_form, name='submit_student'),
    path('student/<str:student_name>/', views.student_detail, name='student_detail'),
    path('students_list/', views.students_list, name='students_list'),
    
]
