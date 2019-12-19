from django.urls import path, include
from . import views
from crasthe.agenda.api.views import *

app_name = 'agenda'

urlpatterns = [
    path('get_horarios/',GetHorariosApiView.as_view(),name='gethorarios-api'),
]