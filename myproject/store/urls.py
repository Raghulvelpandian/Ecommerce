from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('products/', views.get_products),
    path('signup/', views.signup),
    path('login/', TokenObtainPairView.as_view()),   
]