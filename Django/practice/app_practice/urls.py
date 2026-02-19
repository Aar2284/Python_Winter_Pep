from django.urls import path
from . import views

urlpatterns = [
    path('', views.home1),
    path('<str:name>/', views.greet),
    path('student/<str:name>/', views.student_view, name='student'),
]
