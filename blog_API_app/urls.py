from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogAPIView.as_view()),
    path('notes/', views.NoteListCreateAPIView.as_view()),
    path('notes/<int:pk>', views.NoteDetailedAPIView.as_view()),
]
