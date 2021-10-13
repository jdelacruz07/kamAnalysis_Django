from django.urls import path
from . import views

app_name = 'analysis'
urlpatterns = [
    path('gap', views.get_gaps, name='gap'),
    path('gap/add', views.add_gap, name='add'),
    path('gap/<int:gap_id>', views.delete_gap, name='delete'),
]
