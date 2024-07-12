from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from network.models import Seller, Contact, Product
from network.serializers import SellerSerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet


class SellerCreateApiView(CreateAPIView):
    """Класс для создания продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    # def perform_create(self, serializer):
    #     module = serializer.save()
    #     module.owner = self.request.user
    #     module.save()


class SellerListApiView(ListAPIView):
    """Класс для вывода списка продавцов."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerRetrieveApiView(RetrieveAPIView):
    """Класс для подробной информации конкретного продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerUpdateApiView(UpdateAPIView):
    """Класс для редактирования продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerDestroyApiView(DestroyAPIView):
    """Класс для удаления продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
