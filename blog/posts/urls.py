from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    path('Posts/<str:pk>', views.Posts, name='Posts')
]
