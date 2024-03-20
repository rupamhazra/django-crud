from django.urls import path
from . import views
    
urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("student_registration/", views.student_registration, name="student_registration"),
    path("change_password/", views.change_password, name="change_password"),
    path("student_login/", views.student_login, name="student_login"),
    path("logout/", views.Logout, name="logout"),
    path("admin_login/", views.admin_login, name="admin_login"),
    
]    