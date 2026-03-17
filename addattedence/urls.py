from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddAttedenceView

router = DefaultRouter()
router.register(r'addattedence',AddAttedenceView)

urlpatterns = [
    path('', include(router.urls)),
]