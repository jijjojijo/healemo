from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('quiz/<slug:slug>/', views.quiz_detail, name='quiz_detail'),
    path('quizs/', views.quiz_list, name='quiz_list'),
    path('result/<str:code>/', views.get_result, name='result'),
    path('create-result/', views.result_create, name='create-result'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
