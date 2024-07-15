from rest_framework.serializers import ModelSerializer

from network.models import Seller, Contact, Product


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SellerSerializer(ModelSerializer):
    contact = ContactSerializer()
    product = ProductSerializer()

    class Meta:
        model = Seller
        fields = "__all__"


class SellerUpdateSerializer(ModelSerializer):
    contact = ContactSerializer()
    product = ProductSerializer()

    class Meta:
        model = Seller
        exclude = ["debt"]
