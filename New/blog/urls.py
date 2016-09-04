from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from blog import views


router = SimpleRouter()
router.register(r'posts', views.PostViewSet, base_name='posts')
urlpatterns = router.urls



urlpatterns = [
    # ex: /polls/
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]
