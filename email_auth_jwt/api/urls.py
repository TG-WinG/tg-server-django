from django.urls import path,include
from . import views

urlpatterns=[
    path('activate/<str:uidb64>/<str:token>',views.activate, name='activate'),
    path('send_email/',views.send_email,name='send_email'),
]
