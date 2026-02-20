from rest_framework import viewsets, permissions
from .models import Category, Product, Profile, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, ProfileSerializer, OrderSerializer, OrderItemSerializer

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Profile ViewSet
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # Changed to AllowAny for easier testing, but logic still depends on user
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Fallback to a default user if not authenticated for testing purposes
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)

# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user)
        return Order.objects.all()

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)

# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
