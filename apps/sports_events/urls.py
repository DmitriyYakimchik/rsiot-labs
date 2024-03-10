from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RaceViewSet, RacerViewSet, CarViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'races', RaceViewSet)
router.register(r'racers', RacerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]