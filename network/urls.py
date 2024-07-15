from django.urls import path
from rest_framework.routers import SimpleRouter
from network.apps import NetworkConfig
from network.views import (
    SellerListApiView,
    SellerRetrieveApiView,
    SellerCreateApiView,
    SellerDestroyApiView,
    SellerUpdateApiView,
    ProductListApiView,
    ProductRetrieveApiView,
    ProductCreateApiView,
    ProductDestroyApiView,
    ProductUpdateApiView,
    ContactViewSet,
)

app_name = NetworkConfig.name
router = SimpleRouter()
router.register(r"contacts", ContactViewSet)

urlpatterns = [
    path("seller/", SellerListApiView.as_view(), name="seller-list"),
    path(
        "seller/retrieve/<int:pk>/",
        SellerRetrieveApiView.as_view(),
        name="seller-retrieve",
    ),
    path("seller/create/", SellerCreateApiView.as_view(), name="seller-create"),
    path(
        "seller/delete/<int:pk>/", SellerDestroyApiView.as_view(), name="seller-delete"
    ),
    path(
        "seller/update/<int:pk>/", SellerUpdateApiView.as_view(), name="seller-update"
    ),
    path("product/", ProductListApiView.as_view(), name="product-list"),
    path(
        "product/retrieve/<int:pk>/",
        ProductRetrieveApiView.as_view(),
        name="product-retrieve",
    ),
    path("product/create/", ProductCreateApiView.as_view(), name="product-create"),
    path(
        "product/delete/<int:pk>/",
        ProductDestroyApiView.as_view(),
        name="product-delete",
    ),
    path(
        "product/update/<int:pk>/",
        ProductUpdateApiView.as_view(),
        name="product-update",
    ),
]

urlpatterns += router.urls
