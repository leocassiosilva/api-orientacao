from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from trabalho.views import TrabalhoViewSet
from tarefa.views import TarefaViewSet
from accounts.views import UsuarioViewSet
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'trabalhos', TrabalhoViewSet)
router.register(r'tarefas', TarefaViewSet)
router.register(r'accounts', UsuarioViewSet)
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
