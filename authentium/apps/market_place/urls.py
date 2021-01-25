from django.urls import path

from authentium.apps.market_place.views.market_place import ViewMarketPlace
from authentium.apps.market_place.views.product_detail import ViewMarketPlaceProductDetail
from authentium.apps.market_place.views.cart import ViewMarketPlaceCart
from authentium.apps.market_place.views.cart_thanks import ViewMarketPlaceCartThanks
from authentium.apps.market_place.views.cart_checkout import ViewMarketPlaceCartCheckout

urlpatterns = [

    path('market-place/', 
         ViewMarketPlace.as_view(),
         name='market-place'
    ),

    path('product-detail/<int:pk>', 
         ViewMarketPlaceProductDetail.as_view(),
         name='product-detail'
    ),

    path('cart/<int:pk>', 
         ViewMarketPlaceCart.as_view(),
         name='cart'
    ),
    
    path('cart-checkout/', 
         ViewMarketPlaceCartCheckout.as_view(),
         name='cart-checkout'
    ),
    
    path('cart-thanks/', 
         ViewMarketPlaceCartThanks.as_view(),
         name='cart-thanks'
    ),

]