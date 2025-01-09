from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import MenuItem, Review, Subscription
from .serializers import UserSerializer, MenuItemSerializer, ReviewSerializer, SubscriptionSerializer

class SubscriptionCreate(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create the user
        user = User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password')
        )

        # Create token
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginView(APIView):
    def post(self, request):
        # Get the username, email, and password from request data
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if both username/email and password are provided
        if not (username or email) or not password:
            return Response({'message': 'Username/email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Try to get the user by either username or email
        user = None
        if email:  # If email is provided, use it to get the user
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:  # If username is provided, use it to get the user
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Authenticate using the user and the password
        if user and user.check_password(password):
            return Response({'message': 'Login successful'})
        
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        # Handle image field properly
        image = self.request.data.get('image', None)
        serializer.save(image=image)

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # Associate the review with the currently authenticated user
        serializer.save(user=self.request.user)
