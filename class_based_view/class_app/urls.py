from django.conf.urls import url
from django.urls import path
from class_app import views

app_name='class_app'

urlpatterns = [
    path('',views.indexView.as_view(),name="index" ),
    path('indexList/',views.indexListView.as_view(),name="indexList" ),
    path('musicianDetail/<pk>',views.musicianDetails.as_view(),name="musicianDetail" ),
    path('musicianAdd/',views.addMusician.as_view(),name="musicianAdd" ),
    path('musicianUpdate/<pk>',views.updateMusician.as_view(),name="musicianUpdate" ),
    path('musicianDelete/<pk>',views.deleteMusician.as_view(),name="musicianDelete" ),
    ]
