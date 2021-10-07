from django.urls import path
from .views import *

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('v1/',Create.as_view(),name='create'),
    path('v2/',Read.as_view(),name='read'),
    path('v3/<int:id>/',Update.as_view(),name='update'),
    path('v4/<int:id>/',Delete.as_view(),name='delete'),
    path('v5/',Log_In.as_view(),name='login'),
    path('v6/',Log_Out.as_view(),name='logout'),
    path('v7/',Register.as_view(),name='register')
]