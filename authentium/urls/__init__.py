"""authentium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from authentium import settings
from django.conf.urls.static import static
from authentium.apps.account.views.user_short_url import ViewAccountShortUrl
from authentium.apps.account.views.logout import ViewAccountLogout

urlpatterns = [

    path('admin/', 
        admin.site.urls
    ),

    path('logout/',
         ViewAccountLogout.as_view(),
         name='logout'
    ),

    path('',
         include(('authentium.apps.site.urls', 'site'), namespace='site')
    ),

    path('',
         include(('authentium.apps.account.urls', 'account'), namespace='account')
    ),

    path('',
         include(('authentium.apps.market_place.urls', 'market_place'), namespace='market_place')
    ),

    path('api/v0.1/',
         include(('authentium.urls.api', 'api'), namespace='api')
    ),

    path('o/', 
        include('oauth2_provider.urls', namespace='oauth2_provider')
    ),

    path('<slug:path>/',
         ViewAccountShortUrl.as_view(),
         name='user-short-url'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
