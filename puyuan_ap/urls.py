from django.urls import path
from . import views

urlpatterns = [
    # 註冊
    path("/register", views.register, name="register"),

    # 登入
    path("/auth", views.auth),

    # 發送驗證碼
    path("/verification/send", views.verification_send, name="send"),

    # 驗證驗證碼
    path("/verification/check", views.verification_check, name="check"),

    # 忘記密碼
    path("/password/forgot", views.forget_pwd, name="forgot"),

    # 重設密碼
    path("/password/reset", views.reset_password, name="reset"),

    # 註冊確認
    path("/register/check", views.register_check, name="register_confirm"),
    
    # 最新消息
    path("/news", views.news, name="get_news")
]