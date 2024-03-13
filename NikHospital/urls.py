from django.urls import path
from . import views
from .views import home_page,registration
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('',views.login,name='login'),
    # path('home_page',views.home_page,name='home_page'),
    path('home_page/', views.home_page, name='home_page'),
    path('register',views.registration,name='registration'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('doct1',views.doct1,name='doct1'),
    path('doct2',views.doct2,name='doct2'),
    path('doct3',views.doct3,name='doct3'),
    path('doct4',views.doct4,name='doct4'),
    path('doct5',views.doct5,name='doct5'),
    path('doct6',views.doct6,name='doct6')
]