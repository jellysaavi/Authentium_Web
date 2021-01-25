from django.urls.conf import path
from authentium.apps.account.api.views.login import ViewAPIAccountLogin
from authentium.apps.account.api.views.buyer import ViewAPIAccountRegistrationBuyer
from authentium.apps.account.api.views.seller import ViewAPIAccountRegistrationSeller
from authentium.apps.account.api.views.driver import ViewAPIAccountRegistrationDriver
from authentium.apps.account.api.views.forgot_password import ViewAPIAccountFrogotPassword
from authentium.apps.account.api.views.verify_user import ViewAPIAccountVerifyUser
from authentium.apps.account.api.views.verify_prd_token import ViewAPIAccountVerifyPRDToken
from authentium.apps.account.api.views.prd_token_assign import ViewAPIAccountAssignPRDToken
from authentium.apps.account.api.views.update_order import ViewAPIAccountUpdateOrder

urlpatterns = [
    
    path('login', 
         ViewAPIAccountLogin.as_view(), 
         name='login'
    ),

    path('register/buyer', 
         ViewAPIAccountRegistrationBuyer.as_view(), 
         name='register-buyer'
    ),

    path('register/seller', 
         ViewAPIAccountRegistrationSeller.as_view(), 
         name='register-seller'
    ),

    path('register/driver', 
         ViewAPIAccountRegistrationDriver.as_view(), 
         name='register-driver'
    ),
    
    path('verify/user', 
         ViewAPIAccountVerifyUser.as_view(), 
         name='verify-user'
    ),
    
    path('verify/prd', 
         ViewAPIAccountVerifyPRDToken.as_view(), 
         name='verify-prd'
    ),
    
    path('assign/prd', 
         ViewAPIAccountAssignPRDToken.as_view(), 
         name='assign-prd'
    ),
     
    path('forgot-password/', 
         ViewAPIAccountFrogotPassword.as_view(),
         name='forgot-password'
    ),
    
    path('update-order/', 
         ViewAPIAccountUpdateOrder.as_view(),
         name='update-order'
    ),

]
