# TG-Server-Django: Django를 이용한 이메일 인증서비스

TG-Server-Django는 Django와 SMTP을 이용하여 이메일 인증을 하는 프로젝트입니다.  
사용자는 이메일 인증을 통해 JWT토큰을 발급받을 수 있습니다.

## Auth 폴더

Auth 폴더는 사용자 인증과 관련된 기능을 담당합니다.   
이 폴더에는 사용자 인증을 위한 모델, 뷰, URL 패턴 등이 구현되어 있습니다.

## email_auth_jwt 폴더

email_auth_jwt 폴더는 JWT(JSON Web Token)를 이용하여 이메일 인증을 구현한 폴더입니다.  
이 폴더에는 이메일 인증을 위한 모델, 뷰, URL 패턴 등이 구현되어 있습니다.

## 요구사항 및 의존성

TG-Server-Django를 실행하기 위해서는 다음 명령어를 실행해주세요.
``` pip install -r requirements.txt ```

## 실행방법
1. 프로젝트를 다운로드합니다.  
   ``` git clone https://github.com/TG-WinG/tg-server-django.git ```  
2. 프로젝트 폴더로 이동해서 가상 환경을 생성하고 이를 활성화 합니다.  
    ```cd tg-server-django```  
   ```python -m venv venv```  
   ```source venv/bin/activate```  
3. 필요한 패키지를 설치합니다.
   ```pip install -r requirements.txt```
4. Django 서버를 실행합니다.
   ```python manage.py runserver``` 
