from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response(
                {
                    'message': 'User registered successfully',
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        
        if user is not None:
            # Authenticate the user using Django's login function
            login(request, user)
            
            # Generate access and refresh tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
             
            # Serialize the user object, excluding the password field
            user_data = UserRegistrationSerializer(user).data
            user_data.pop('password', None)  # Remove the 'password' field
            user_data.pop('is_superuser', None)  # Remove the 'password' field
            
            return Response(
                {
                    'message': 'Login successful',
                    'user': user_data,  # Serialize the user object
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                },
                status=status.HTTP_200_OK,
            )
    
    return Response(
        {'error': 'Invalid credentials'},
        status=status.HTTP_401_UNAUTHORIZED,
    )
 


 
@api_view(['POST']) 
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def addticket(request):
    if request.method == 'POST':
         
        return Response(
            {
                'message': 'YOU ARE AUTHORIZED ',
                'user': request.user.email,  # Access the user's ID
            },
            status=status.HTTP_201_CREATED,
        )



@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    # Invalidate tokens (optional, can also revoke tokens by blacklisting)
    request.auth = None  # Remove authentication
    request.session.flush()  # Flush session data

    return Response(
        {'message': 'Logout successful'},
        status=status.HTTP_200_OK,
    )





 