from . import views
from django.urls import path

urlpatterns = [
    path('create-weight', views.createWeight.as_view(), name='create weight'),
    path('update-weight', views.updateWeight.as_view(), name='update weight'),
    path('delete-weight', views.deleteWeight.as_view(), name='delete weight'),
    path('all-weight', views.AllWeightView.as_view(), name='all weight'),
]
