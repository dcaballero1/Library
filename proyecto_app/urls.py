from rest_framework import routers
from .api import bookViewSet, printingViewSet, readerViewSet, bookstoreViewSet

router= routers.DefaultRouter()

router.register('api/book', bookViewSet, 'book')
router.register('api/printing', printingViewSet, 'printing')
router.register('api/reader', readerViewSet, 'reader')
router.register('api/bookstore', bookstoreViewSet, 'bookstore')

urlpatterns = router.urls