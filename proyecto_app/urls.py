from rest_framework import routers
from .api import libroViewSet, imprentaViewSet, lectorViewSet, bibliotecaViewSet

router= routers.DefaultRouter()

router.register('api/libro', libroViewSet, 'libro')
router.register('api/imprenta', imprentaViewSet, 'imprenta')
router.register('api/lector', lectorViewSet, 'lector')
router.register('api/biblioteca', bibliotecaViewSet, 'biblioteca')

urlpatterns = router.urls