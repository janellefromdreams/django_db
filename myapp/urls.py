from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Root URL for the homepage
    path('persons/', views.person_list, name='person_list'),  # URL for the persons list
]
