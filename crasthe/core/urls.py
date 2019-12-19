from django.urls import path, include
from . import views
from crasthe.core.api.views import *

app_name = 'core'

urlpatterns = [
    path('a/status/',StatusApiView.as_view(),name='status-api'),
    path('', views.index, name='index'),
    #path('documentacao/', schema_view),
]