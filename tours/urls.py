from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Mainview'),
    path('departure/<str:departure>', views.DepartureView.as_view(), name='DepartureView'),
    path('tour/<int:id>', views.TourView.as_view(), name='TourView'),
]
