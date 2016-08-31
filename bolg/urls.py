from django.conf.urls import url, patterns, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from bolg import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='posts')
router.register(r'comments', views.CommentViewSet, base_name='comments')
urlpatterns = router.urls



urlpatterns = [
    # ex: /polls/
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    ]
