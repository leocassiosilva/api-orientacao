from django.contrib import admin
from django.urls import path, include
from trabalho.views import TrabalhoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'trabalhos', TrabalhoViewSet)
router.register(r'tarefas', TrabalhoViewSet)
router.register(r'accounts', TrabalhoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))

]
