from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls