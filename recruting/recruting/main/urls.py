from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter


from recruting.main import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('reg/', views.RegistrationView.as_view()),
    path('logout/', views.logout)
]

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns += router.urls