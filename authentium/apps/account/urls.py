from django.urls import path
from authentium.apps.account.views.user_qr_code import ViewAccountUserQrCode
from authentium.apps.account.views.dashboard import ViewAccountDashboard
from authentium.apps.account.views.product import ViewProduct
from authentium.apps.account.views.product_list import ViewProductList
from authentium.apps.account.views.product_delete import ViewProductDelete
from authentium.apps.account.views.order_list import ViewOrderList
from authentium.apps.account.views.order_consignment import ViewOrderConsignment
from authentium.apps.site.views.login import ViewSiteLogin
from authentium.apps.account.views.order_map_view import ViewOrderMapView
from authentium.apps.account.views.test import ViewAccountTest

urlpatterns = [

    path('dashboard/',
         ViewAccountDashboard.as_view(),
         name='dashboard'
    ),
    
    path('product/',
         ViewProduct.as_view(),
         name='product'
    ),
    
    path('product-list/',
         ViewProductList.as_view(),
         name='product-list'
    ),
    
    path('product/delete/<int:pk>',
         ViewProductDelete.as_view(),
         name='product-delete'
    ),

    path('user/qr-code/info/',
         ViewAccountUserQrCode.as_view(),
         name='user-qr-code'
    ),
    
    path('order-list/',
         ViewOrderList.as_view(),
         name='order-list'
    ),

        
    path('order-consignment/<int:pk>',
         ViewOrderConsignment.as_view(),
         name='order-consignment'
    ),

    path('accounts/login/',
         ViewSiteLogin.as_view(),
         name='login'
    ),

            
    path('order-map-view/<int:pk>',
         ViewOrderMapView.as_view(),
         name='order-map-view'
    ),
    
    path('test',
         ViewAccountTest.as_view(),
         name='test'
    ),
]
