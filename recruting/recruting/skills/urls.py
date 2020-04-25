from django.urls import path

from recruting.skills.views import DepartmentListAPIView

urlpatterns = [
    path('departments/', DepartmentListAPIView.as_view())
]