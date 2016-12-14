"""coosta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .routers import router
from properties import views
from django.conf import settings
from django.conf.urls.static import static

from properties.views import  save_property,zillow_api


admin.site.site_title = 'Coosta'
admin.site.site_header = 'Coosta'
# admin.site.index_title = 'Admin Page'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^user/', include('coosta_users.urls')),
    url(r'^property/', include('properties.urls')),
    url(r'^user/login/$', auth_views.login, name='login', kwargs={'redirect_authenticated_user': True}),
    url(r'^user/logout/$', auth_views.logout, name='logout'),
    url(r'^save_property/$',save_property),
    url(r'^zillow_api/$',zillow_api),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()