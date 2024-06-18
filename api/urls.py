from django.urls import path, include
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewset

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employee', EmployeeViewset)

urlpatterns = [
    path('', include(router.urls)),
]