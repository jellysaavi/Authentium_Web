from django.urls.conf import include
from django.urls.conf import path


urlpatterns = [
  
    path('account/', 
        include(
             ('authentium.apps.account.api.urls', 'account'), 
             namespace='account'
        )
    ),
        
]
