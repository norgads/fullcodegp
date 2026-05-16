from django.urls import path

from . import views

urlpatterns = [
    path('<int:game_id>/add_to_library/', views.add_to_library, name='add_to_library'),
    path('<int:game_id>/remove_from_library/', views.remove_from_library, name='remove_from_library'), 
    path('', views.user_library, name='user_library'),
]