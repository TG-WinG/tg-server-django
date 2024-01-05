from django.shortcuts import render, redirect
from .models import CustomUser as User
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.http import HttpResponse,JsonResponse
import requests, time



def send_email(request):
    #포스트 방식인지 확인
    if request.method=='POST':
        auth_name=request.POST['name']
        auth_student_id=request.POST['student_id']
        auth_pw=request.POST['password']
        auth_email=request.POST['email']
        user=authenticate(email=auth_email,password=auth_pw) #유저 인증
        if(user==None):#유저가 존재하지 않는 경우
            return JsonResponse({"Status":"Fail","Message":"User does not exist"})
        elif(user.name!=auth_name) or (user.student_id!=auth_student_id):#유저가 존재하지 않는 경우
            return JsonResponse({"Status":"Fail","Message":"User information is not correct"})
        current_site=get_current_site(request) #현재 사이트 정보 가져오기
        #메시지 발송
        message = render_to_string('mail/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.name)),
            'token': account_activation_token.make_token(user),
        })
        mail_title = "계정 활성화 확인 이메일"
        mail_to = user.email
        email = EmailMessage(mail_title, message, to=[mail_to])
        email.send()
        #인증 완료 메시지
        return JsonResponse({"Status":"Success","Message":"Please check your email and complete authentication."})
    else: return render(request,'mail/send.html')
        
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(name=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None
            return JsonResponse({"Status":"Fail","Message":"Error"})
    if not(user==None) : # 인증하려는 링크가 유효한 링크라면 토큰 발행
        user.is_email_activated = True
        user.save()
        return JsonResponse({"Status":"Success"})
    else:
        return JsonResponse({"Status":"Fail","Message":"Link is not valid"})
    return 

