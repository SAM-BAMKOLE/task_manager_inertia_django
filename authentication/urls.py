from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name="authentication.login"),
    path('register/', register_page, name="authentication.register"),
    path('logout/', logout_page, name="authentication.logout"),
    path('forgot-password/', forgot_password_page, name="authentication.forgot_password"),
    path('profile/', profile_page, name='authentication.profile'),
]