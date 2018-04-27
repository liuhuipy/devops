"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
# from rest_framework.authtoken import views as auth_views
from django.conf import settings
import xadmin



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'', include('dashboard.urls')),
    url(r'^accounts/', include('accounts.urls.view_urls', namespace='accounts')),
    url(r'^assets/', include('assets.urls.view_urls', namespace='assets')),
    url(r'^permission/', include('permission.urls.view_urls', namespace='permission')),
    url(r'^ops/', include('ops.urls.view_urls', namespace='ops')),
    url(r'^audit/', include('audit.urls', namespace='audit')),

    # api
    url(r'^', include('assets.urls.api_urls')),
    url(r'^', include('accounts.urls.api_urls')),
    # url(r'api-token-auth/', auth_views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
