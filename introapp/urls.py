from django.urls import include, path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import admin

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('inicio/',views.inicio,name="inicio"),
    path('admin/', admin.site.urls),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>', views.darlike, name='dar_like'),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),]