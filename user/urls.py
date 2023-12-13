from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('<int:user_id>/<str:page_id>/', views.user, name='user'),
    #path('<str:page_id>/', views.my, name='my'),
    #path('settings/<int:id>/', views.settings, name='settings'),
    path('<int:user_id>/', views.user_home, name='user_home'),
    path('<str:page_id>/', views.my, name='my'),
    path('', views.my_home, name='my_home'),
    path('edit_page/<int:id>', views.edit_page, name='edit_page')
]
