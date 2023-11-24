from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session 
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.db.models.functions import ExtractHour
from django.db.models import Q
from django.template import loader
from puyuan_pj.settings import SECRET_KEY
from datetime import datetime
from .models import *
from email.mime.text import MIMEText
from email.header import Header
from django.core.mail import send_mail
import jwt, random, smtplib, string, json
import requests
from django.urls import reverse
from django.utils.crypto import get_random_string
from datetime import datetime
import time
import jsonpickle
from django.views.decorators.http import require_GET
# Create your views here.

#smtp信箱
def send_mail(target_email, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('Zkzcfg8520@gmail.com', 
                    'ldydrwzgygodaptz')
    server.sendmail('Zkzcfg8520@gmail.com', 
                    target_email, msg)
    server.quit()

# 1-1 帳號
#1 註冊
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        length = 6
        invite_code = ''.join(str(random.randint(0, 9)) for _ in range(length))
        register_info.objects.create(
            email=email, 
            password=make_password(password), 
            invite_code=invite_code, 
            created_at=datetime.now()
        )
        get_id = register_info.objects.filter(email=email).values()[0]['id']
        default_info.objects.create(user_id=get_id)
        setting_info.objects.create(user_id=get_id)
        vip_info.objects.create(user_id=get_id, created_at=datetime.now())
        medical_info.objects.create(user_id=get_id)
        a1c_info.objects.create(user_id=get_id)
        message_info.objects.create(user_id=get_id)
        friends_requests.objects.create(user_id=get_id)
        return JsonResponse({"status": "0", "message": "成功"})

#2 登入
def auth(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            email = data['email']
            password = data['password']
            if check_password(password, register_info.objects.filter(email=email).values()[0]['password']):
                if register_info.objects.filter(email=email, state=1).exists():
                    id = register_info.objects.filter(email=email).values()[0]['id']
                    session_id = SessionStore()
                    session_id.create()
                    session_id['id'] = id
                    session_id.save()
                    login_times = register_info.objects.filter(email=email).values()[0]['login_times']
                    register_info.objects.filter(email=email).update(
                        updated_at=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), 
                        login_times=login_times + 1
                    )
                    return JsonResponse({"status": "0", 
                                        "message": "成功",
                                        "token": session_id.session_key})
                else:
                    return JsonResponse({"status": "2", "message": "信箱未驗證"})
            else:
                return JsonResponse({"status": "1", "message": "失敗", "token": ""})
        except IndexError:
            return JsonResponse({"status": "1", "message": "失敗", "token": ""})
            
#3 寄送驗證碼
def verification_send(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            if register_info.objects.filter(email=email).exists():
                verification_code = get_random_string(length=6)
                msg = ("Subject:驗證碼\n\n你的驗證碼是" + verification_code).encode('utf-8')
                send_mail(email, msg)
                register_info.objects.filter(email=email).update(verification_code=verification_code)
                return JsonResponse({"status": "0", "message": "成功"})
        except Exception as e:
            return JsonResponse({"status": "1", "message": "失敗"})

#4 檢查驗證碼
def verification_check(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            code = data['code']
            if register_info.objects.filter(
                email=email, 
                verification_code=code
            ).exists():
                register_info.objects.filter(email=email).update(state=1)
                return JsonResponse({"status": "0", "message": "成功"})
        except Exception as e:
            return JsonResponse({"status": "1", "message": "失敗"})

#5 忘記密碼
def forget_pwd(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            if register_info.objects.filter(email=email).exists():
                register_info.objects.filter(email=email).update(must_change_password=1)
                new_password = get_random_string(length=8)
                msg = ("Subject:忘記密碼\n\n你的新密碼是" + new_password).encode('utf-8')
                send_mail(email, msg)
                register_info.objects.filter(email=email).update(password=make_password(new_password))
                return JsonResponse({"status": "0", "message": "成功"})
        except Exception as e:
            return JsonResponse({"status": "1", "message": "失敗"})

#6 重置密碼
def reset_password(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            password = data['password']
            session_token = request.headers.get('Authorization').split()[1] #重要
            id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
            register_info.objects.filter(id=id).update(
                password=make_password(password), 
                must_change_password=0
            )
            return JsonResponse({"status": "0", "message": "成功"})
        except Exception as e:
            return JsonResponse({"status": "1", "message": "失敗"})
        
#7 註冊確認
def register_check(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if not register_info.objects.filter(email=email).exists():
            return JsonResponse({"status": "0", "message": "成功"})
        else:
            return JsonResponse({"status": "1", "message": "失敗"})

# 1-2 其他   
#8 最新消息
def news(request):
    if request.method == "GET":
        output = {
            "status": "0",
            "message": "成功",
            "news": []
        }
        get_data = new_info.objects.all().values()
        for data in get_data:
            output["news"].append({
                "id": data["id"],
                "member_id": data["member_id"],
                "group": data["group"],
                "message": data["message"],
                "pushed_at": datetime.strftime(data["pushed_at"], "%Y-%m-%d %H:%M:%S"),
                "created_at": datetime.strftime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.strftime(data["updated_at"], "%Y-%m-%d %H:%M:%S")
            })
        return JsonResponse(output, safe=False)