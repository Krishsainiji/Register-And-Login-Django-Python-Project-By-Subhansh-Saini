from django.urls import path
from .views import register_view, login_view, logout_view, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Home page
    path('register/', register_view, name='register'),  # Registration page
    path('login/', login_view, name='login'),  # Login page
    path('logout/', logout_view, name='logout'),  # Logout page
]
