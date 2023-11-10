from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('administration', views.administration, name='administration'),
    path('news', views.news, name='news'),
    path('<int:pk>/', views.newsdetails, name='newsdetails'),
    path('seniormanagement/<int:image_id>', views.seniormanagement)
    # path('aboutmcss', views.aboutmcss, name='aboutmcss'),
    # path('mcssadministration', views.mcssadministration, name='mcssadministration'),
    # path('news', views.news, name='news'),
    # path('tubmanhigh', views.tubmanhigh, name='tubmanhigh'),#for tubman high schools
    # path('tubman_admin', views.tubman_admin, name='tubman_admin'),
    # path('Schedule', views.Schedule, name='Schedule')

]