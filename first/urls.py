from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signin/', views.sign_in, name='signin'),
    path('signup/', views.sign_up, name='signup'),
    path('join/', views.join, name='join'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('myinfo/keyword/<int:id>/', views.keyword, name='keyword'),
    path('myinfo/-keyword/<int:id>/', views.keyword, name='-keyword'),
    path('page-profile/', views.page_profile, name='page_profile'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
    ]