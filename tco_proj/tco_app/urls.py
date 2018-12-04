from django.urls import path
from . import views
from .views import all_json_models
from .templatetags import system_select

urlpatterns = [
    path('', views.index, name='index-page'),
    path('teste_page', views.modelsNames, name='teste-page'),
    path('filter_model', system_select, name='teste-page'),
    path('brand/<int:pk>/all_json_models/', views.all_json_models, name='filter-models-page'),
    # path('tco_app/about.html', views.index, name='index'),
]