
from . import views as core_views
from django.urls import path

urlpatterns = [
    path('', core_views.index, name='index'),
]
