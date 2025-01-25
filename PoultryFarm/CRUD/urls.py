from django.urls import path

from CRUD import views

urlpatterns= [
    path('farms/', views.FarmView.as_view(), name= 'farm')
    path('chicken/<int:pk>', views.SingleChickenView.as_view(), name='single-chicken')
]
