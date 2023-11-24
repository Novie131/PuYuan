from django.urls import path
from . import views

urlpatterns = [
    # 獲取控糖團邀請碼
    path("/code", views.friend_code, name="friend_code"),
    # 控糖團列表 
    path("/list", views.friends_list, name="friends_list"),
    # 獲取控糖團邀請
    path("/requests", views.friend_requests, name="friend_requests"),
    # 送出控糖團邀請
    path("/send", views.friend_send, name="friend_send"),
    # 接受控糖團邀請
    path("/<int:inviteld>/accept", views.invite_accept, name="accept_request"),
    # 拒絕控糖團邀請
    path("/<int:inviteld>/refuse", views.invite_refuse, name="refuse_request"),
    # 刪除更多好友
    path("/remove", views.invite_remove, name="invite_remove"),
    # 控糖團結果
    path("/results", views.friend_result, name="friend_result"),
]