from django.urls import path
from . import views

urlpatterns = [
    # 設定個人資料、(取得)個人資訊
    path("", views.user, name="user"),
    path("/", views.user, name="user"),

    # 設定個人預設值
    path("/default", views.user_default, name="user_default"),

    # 設定個人設定
    path("/setting", views.user_setting, name="user_setting"),

    # 上傳血壓測量結果
    path("/blood/pressure", views.blood_pressure, name="blood_pressure"),

    # 上傳體重測量結果
    path("/weight", views.body_weight, name="body_weight"),

    # 上傳血糖
    path("/blood/sugar", views.blood_sugar, name="blood_sugar"),

    # 日記列表資料
    path("/diary", views.user_diary, name="user_diary"),

    # 飲食日記
    path("/diet", views.user_diet, name="user_diet"),

    # 獲取關懷諮詢, 發送關懷諮詢
    path("/care", views.cares, name="cares"),

    # 就醫資訊, 更新就醫資訊
    path("/medical", views.medical, name="medical"),

    # 糖化血色素, 送糖化血色素, 刪除糖化血色素
    path("/a1c", views.user_a1c, name="user_a1c"),

    # 藥物資訊, 上傳藥物資訊, 刪除藥物資訊
    path("/drug-used", views.drug_used, name="drug_used"),

    # 更新badge
    path("/badge", views.badge, name="badge"),
    
    # 刪除日記記錄, 上一筆紀錄資訊
    path("/records", views.user_records, name="user_records"),
]