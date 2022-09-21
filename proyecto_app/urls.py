from rest_framework import routers
from .api import libroViewSet
router= routers.DefaultRouter()

router.register('api/libro', libroViewSet, 'libro')

urlpatterns = router.urls