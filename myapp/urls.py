
from django.urls import path
from myapp import views
from .views import logoutuser


urlpatterns = [
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/', views.Login, name='login'),
    path('logout/',logoutuser,name='logout')


]
