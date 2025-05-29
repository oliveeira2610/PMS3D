from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SupplierViewSet, MaterialViewSet, PrinterViewSet,
    PartViewSet, PrintJobViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'materials', MaterialViewSet, basename='material')
router.register(r'printers', PrinterViewSet, basename='printer')
router.register(r'parts', PartViewSet, basename='part')
router.register(r'printjobs', PrintJobViewSet, basename='printjob')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

