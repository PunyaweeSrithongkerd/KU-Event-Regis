from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('registered/', views.RegisterView.as_view(), name='register'),
    path('<int:pk>/regis/', views.regis, name='regis'),
    path('<int:pk>/unregis/', views.unregis, name='unregis'),
    url('signup/', views.signup, name='signup'),
]
