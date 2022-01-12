from django.urls import path
from . import views

urlpatterns =[
    path('add/',views.addaddressview.as_view(),name='add_address'),
    path('show/',views.showaddressview.as_view(),name='show_address'),
    path('delete/<int:i>/', views.deleteaddressview.as_view(), name='delete_address'),
    path('update/<int:i>/', views.updateaddressview.as_view(), name='update_address'),

]