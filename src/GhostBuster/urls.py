from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from doctors.views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctor', DoctorViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GhostBuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
)
