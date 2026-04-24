from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.models import User



@api_view(['GET'])
def get_products(request):
    products = Product.objects.all().values()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def signup(request):
    username = request.data['username']
    password = request.data['password']
    if not username or not password:
        return Response({"error": "Username and password required"})


    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"})

    
    user = User.objects.create_user(username=username, password=password)

    return Response({"message":"User created"})