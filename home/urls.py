from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('garments/', views.GarmentListView.as_view(), name='garments'),
    path('garment/<int:pk>', views.GarmentDetailView.as_view(), name='garment_detail'),
]
