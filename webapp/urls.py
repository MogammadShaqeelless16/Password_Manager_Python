
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD

    path('dashboard', views.dashboard, name="dashboard"),

    path('password-generator', views.generate_password, name="password-generator"),

    path('password-health', views.password_health, name="password-health"),

    path('password-encrypt', views.password_encrypt, name="password-encrypt"),

    path('profile', views.profile, name="profile"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    

]






