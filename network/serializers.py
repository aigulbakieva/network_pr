from rest_framework.serializers import ModelSerializer

from network.models import Seller, Contact, Product


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
