from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TakeAttedenceView

router = DefaultRouter()
router.register(r'takeattedence',TakeAttedenceView)

urlpatterns = [
    path('', include(router.urls)),
]