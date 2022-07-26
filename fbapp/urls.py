from django.urls import path
from . import views
urlpatterns=[
    path('fb',views.fbpage,name='fbhomepage')
]