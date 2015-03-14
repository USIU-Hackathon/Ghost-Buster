from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from doctors.views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctor', DoctorViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^$', 'doctors.views.home', name='home'),
    url(r'^(?P<speciality>[\w\-]+)/$', 'doctors.views.get_by_speciality', name='speciality'),
    url(r'^(?P<name>[\w\-]+)/$', 'doctors.views.get_by_name', name='name'),
    )
