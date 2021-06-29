from django.urls import path 
from .views import PostHome


urlpatterns = [
    path('',PostHome.as_view(),name='home'),

]
