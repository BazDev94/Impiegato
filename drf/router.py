from impiegato.api.viewsets import ImpiegatoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'impiegato', ImpiegatoViewSet)
urlpatterns = router.urls


for url in router.urls:
     print(url, '\n')