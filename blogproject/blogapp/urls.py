from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_view, name="register_view"),
    path('login/', views.login_view, name="login_view"),
    path('detail/<int:id>/', views.blogdetail, name="blogdetail"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
    path('update_post/<int:id>/', views.update_post, name="update_post"),
    path('logout/', views.logout_view, name="logout_view"),
    path('profile/', views.profile_page, name="profile_page"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
   
   
  
    
]