from django.urls import path
from rest_framework.routers import SimpleRouter
from network.apps import NetworkConfig
from network.views import SellerListApiView, SellerRetrieveApiView, SellerCreateApiView, SellerDestroyApiView, \
    SellerUpdateApiView, ProductViewSet

app_name = NetworkConfig.name
router = SimpleRouter()
router.register(r"network/products", ProductViewSet)

urlpatterns = [
    path("", SellerListApiView.as_view(), name="seller-list"),
    path("<int:pk>/", SellerRetrieveApiView.as_view(), name="seller-retrieve"),
    path("create/", SellerCreateApiView.as_view(), name="seller-create"),
    path("delete/<int:pk>/", SellerDestroyApiView.as_view(), name="seller-delete"),
    path("update/<int:pk>/", SellerUpdateApiView.as_view(), name="seller-update"),
]

urlpatterns += router.urls
