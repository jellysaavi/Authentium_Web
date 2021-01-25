from django.urls import path
from authentium.apps.site.views.login import ViewSiteLogin
from authentium.apps.site.views.sign_up import ViewSiteSignUp
from authentium.apps.site.views.buyer_sign_up import ViewSiteBuyerSignUp
from authentium.apps.site.views.seller_sign_up import ViewSiteSellerSignUp
from authentium.apps.site.views.driver_sign_up import ViewSiteDriverSignUp
from authentium.apps.site.views.forgot_password import ViewSiteForgotPassword
from authentium.apps.site.views.register_thanks import ViewSiteRegisterThanks
from authentium.apps.site.views.born_to_track import ViewSiteBornToTrack
from authentium.apps.site.views.delex import ViewSiteDelex
from authentium.apps.site.views.delex_register import ViewSiteDelexRegister
from authentium.apps.site.views.delex_register_driver import ViewSiteDelexRegisterDriver
from authentium.apps.site.views.delex_thanks import ViewSiteDelexThanks
from authentium.apps.site.views.delex_exchange import ViewSiteDelexExchange

urlpatterns = [

    path('',
         ViewSiteLogin.as_view(),
         name='login'
    ),
    
    path('born-to-track',
         ViewSiteBornToTrack.as_view(),
         name='born-to-track'
    ),
    
    path('delex',
         ViewSiteDelex.as_view(),
         name='delex'
    ),

    path('delex-exchange',
         ViewSiteDelexExchange.as_view(),
         name='delex-exchange'
    ),

    path('delex-register',
         ViewSiteDelexRegister.as_view(),
         name='delex-register'
    ),

    path('delex-register-driver',
         ViewSiteDelexRegisterDriver.as_view(),
         name='delex-register-driver'
    ),
    
    path('delex-thanks',
         ViewSiteDelexThanks.as_view(),
         name='delex-thanks'
    ),

    path('sign-up',
         ViewSiteSignUp.as_view(),
         name='sign-up'
    ),

    path('buyer-sign-up',
         ViewSiteBuyerSignUp.as_view(),
         name='buyer-sign-up'
    ),

    path('seller-sign-up',
         ViewSiteSellerSignUp.as_view(),
         name='seller-sign-up'
    ),

    path('driver-sign-up',
         ViewSiteDriverSignUp.as_view(),
         name='driver-sign-up'
    ),
    
    path('register-thanks',
         ViewSiteRegisterThanks.as_view(),
         name='register-thanks'
    ),

    path('forgot-password',
         ViewSiteForgotPassword.as_view(),
         name='forgot-password'
    ),

]
