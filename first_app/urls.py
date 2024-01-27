from django.urls import path
from . import views
urlpatterns = [
    path('set1/', views.set_cookie),
    path('set2/', views.set_session),
    path('get1/', views.get_cookie),
    path('get2/', views.get_session),
    path('del1/', views.delete_cookie),
    path('del2/', views.delete_session)
]
