from django.urls import path

from . import views

urlpatterns = [
      path('articles/', views.PublicationList.as_view()),
]