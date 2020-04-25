from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from recruting.main.views import UserViewSet, RegistrationView, logout

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('reg/', RegistrationView.as_view()),
    # path('change_password/', ChangePasswordAPIView.as_view()),
    path('logout/', logout),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns += router.urls