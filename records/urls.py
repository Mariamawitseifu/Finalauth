# accounts/urls.py

from django.urls import path, include
from .views import register_user, user_login, user_logout
from .views import change_password
from django.conf import settings
from django.conf.urls.static import static 
from .views import record_detail,record_list,record_create,delete_record,update_record,record_search_api

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/records/', record_list, name='record-list'),
    path('api/records/<int:pk>/', record_detail, name='record-detail'),
    path('api/records/create/', record_create, name='record-create'),
    path('api/records/delete/<int:pk>/',delete_record, name='delete_record'),
    path('records/<int:pk>/', update_record, name='update_record'),
    path('api/record/search/', record_search_api, name='record_search_api'),
]