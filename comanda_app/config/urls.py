from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    
     # --- Template Views ---
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('dashboard/', TemplateView.as_view(template_name="base.html"), name="dashboard"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]


 