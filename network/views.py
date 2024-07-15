from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from network.models import Seller, Contact, Product
from network.serializers import SellerSerializer, ProductSerializer, ContactSerializer, SellerUpdateSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from users.permissions import IsActiveUser


class SellerCreateApiView(CreateAPIView):
    """Класс для создания продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsActiveUser,)


class SellerListApiView(ListAPIView):
    """Класс для вывода списка продавцов."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsActiveUser,)


class SellerRetrieveApiView(RetrieveAPIView):
    """Класс для подробной информации конкретного продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsActiveUser,)


class SellerUpdateApiView(UpdateAPIView):
    """Класс для редактирования продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerUpdateSerializer
    permission_classes = (IsActiveUser,)


class SellerDestroyApiView(DestroyAPIView):
    """Класс для удаления продавца."""

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsActiveUser,)


class ProductCreateApiView(CreateAPIView):
    """Класс для создания продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveUser,)


class ProductListApiView(ListAPIView):
    """Класс для вывода списка продуктов."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveUser,)


class ProductRetrieveApiView(RetrieveAPIView):
    """Класс для подробной информации конкретного продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveUser,)


class ProductUpdateApiView(UpdateAPIView):
    """Класс для редактирования продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveUser,)


class ProductDestroyApiView(DestroyAPIView):
    """Класс для удаления продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveUser,)


class ContactViewSet(ModelViewSet):
    """Вьюсет для модели контакт."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("country",)
    permission_classes = (IsActiveUser,)
