from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('update_profile/<int:pk>/', views.update_profile, name='update_profile')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)