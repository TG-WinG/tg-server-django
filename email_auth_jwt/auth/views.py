from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json
from django.contrib.auth.hashers import PBKDF2PasswordHasher


@csrf_exempt
def issue_tokens(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = str(data.get('password'))
    try:
        user = get_user_model().objects.get(email=email)
    except user.DoesNotExist:
        return JsonResponse({"Status":"Fail","Message":"User does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)

    if user.check_password(password)==False:
        return JsonResponse({"Status":"Fail","Message":"Password is not correct"}, 
                            status=status.HTTP_400_BAD_REQUEST)
    elif user.is_email_activated==False:
        return JsonResponse({"Status":"Fail","Message":"User is not activated. Please activate your account first"}, 
                            status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return JsonResponse({'access': access_token, 'refresh': str(refresh)}, status=status.HTTP_200_OK)
