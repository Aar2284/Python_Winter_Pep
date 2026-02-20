from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order, Category, Profile, OrderItem

# Custom field to create the object if it doesn't exist
class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            # get_or_create returns a tuple (object, created)
            obj, created = self.get_queryset().get_or_create(**{self.slug_field: data})
            return obj
        except (TypeError, ValueError):
            self.fail('invalid')

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    # Now automatically creates the category if it doesn't exist
    category = CreatableSlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

# Profile Serializer (OneToOneField -> User)
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

# OrderItem Serializer (ForeignKey -> Product)
class OrderItemSerializer(serializers.ModelSerializer): 
    product = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product_details'] = {
            "id": instance.product.id,
            "name": instance.product.name,
            "price": str(instance.product.price)
        }
        return response

# Order Serializer (ForeignKey -> User, ManyToManyField -> OrderItem)
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = '__all__'
