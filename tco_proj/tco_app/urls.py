from django.urls import path
from django.conf.urls import url
from . import views
from .views import all_json_models
# from .templatetags import system_select

urlpatterns = [
    path('', views.index, name='index-page'),
    path('teste_page', views.modelsNames, name='teste-page'),
    # path('filter_model', system_select, name='filter-models-page'),
    # path('tco_app/<int:pk>/all_json_models/', views.all_json_models),
    path('simulation_page', views.system_choice, name='sims-page'),
    # path('tco_app/about.html', views.index, name='index'),
    # (r’^brand/(?P<brand>[-\w]+)/all_json_models/$’, ‘all_json_models’),
    path('simulation_page/<int:pk>/all_json_models/', views.all_json_models, name='all_json_models'),
    path('simulation_page/<int:pk>/all_json_cpus/', views.all_json_cpus, name='all_json_cpus'),
    path('simulation_page/<int:cpu>/<int:f_maintenance>/<str:currency>/json_simulation/', views.json_simulation, name='json_simulation'),
]