from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    # path('tco_app/about.html', views.index, name='index'),
]