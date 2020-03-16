from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name="reg"),
    path('profile/', userViews.profile, name="profile"),
    path('auth/', authViews.LoginView.as_view(template_name='users/input.html'), name="auth"),
    path('exit/', authViews.LogoutView.as_view(template_name='homepage/home.html'), name="exit"),
    path('', include('homepage.urls')),

]
