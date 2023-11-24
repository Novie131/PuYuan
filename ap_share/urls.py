from django.urls import path
from . import views

urlpatterns = [
    # 分享
    path("", views.share, name="share"),
    
    # 查看分享
    path("/<type>", views.get_share, name="check_share"),
]