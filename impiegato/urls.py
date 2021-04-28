from django.urls import path
from .api import GetApi, PostApi, UpdateApi,DeleteApi

urlpatterns = [

    path('api/',GetApi.as_view()),
    path('api/post',PostApi.as_view()),
    path('api/<int:pk>/update',UpdateApi.as_view()),
    path('api/<int:pk>/delete',DeleteApi.as_view()),
]