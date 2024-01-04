from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json



@csrf_exempt
def issue_tokens(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    User = get_user_model()
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)

    if password!=user.password:
        return JsonResponse({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return JsonResponse({'access': access_token, 'refresh': str(refresh)}, status=status.HTTP_200_OK)
