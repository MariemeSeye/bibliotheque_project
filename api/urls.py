from rest_framework.routers import DefaultRouter
from .views import AuteurViewSet, LivreViewSet, EmpruntViewSet, EtiquetteViewSet

router = DefaultRouter()

router.register('auteurs', AuteurViewSet)
router.register('livres', LivreViewSet)
router.register('emprunts', EmpruntViewSet)
router.register('etiquettes', EtiquetteViewSet)

urlpatterns = router.urls