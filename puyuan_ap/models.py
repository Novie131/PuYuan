from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
# Create your models here.

# 註冊
class register_info(models.Model):
    #註冊
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, default="User")
    account = models.CharField(max_length=30, null=True, default="")
    email = models.CharField(max_length=30, null=True, default="")
    phone = models.CharField(max_length=30, null=True, default="")
    password = models.CharField(max_length=30, null=True, default="")
    state = models.IntegerField(default=0)
    must_change_password = models.IntegerField(default=0)
    status = models.CharField(max_length=30, null=True, default="Normal")
    verification_code = models.CharField(max_length=50, null=True, default="")
    birthday = models.DateField(null=True, default=datetime.datetime.now().strftime("%Y-%m-%d"))
    height = models.FloatField(null=True, default=0.0)
    weight = models.FloatField(null=True, default=0.0)
    gender = models.IntegerField(null=True, default=0)
    address = models.CharField(max_length=30, null=True, default="")
    # 其他
    login_times = models.IntegerField(null=True, default=0)
    privacy_policy = models.IntegerField(null=True, default=1)
    badge = models.IntegerField(null=True, default=0)
    group = models.CharField(max_length=30, null=True, default="")
    fcm_id = models.CharField(max_length=255, null=True, default="")
    pushed_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    # 控糖邀請
    invite_code = models.CharField(max_length=30, null=True, default="")

# 個人預設值
class default_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    sugar_delta_max = models.FloatField(null=True, default=0)
    sugar_delta_min = models.FloatField(null=True, default=0)
    sugar_morning_max = models.FloatField(null=True, default=0)
    sugar_morning_min = models.FloatField(null=True, default=0)
    sugar_evening_max = models.FloatField(null=True, default=0)
    sugar_evening_min = models.FloatField(null=True, default=0)
    sugar_before_max = models.FloatField(null=True, default=0)
    sugar_before_min = models.FloatField(null=True, default=0)
    sugar_after_max = models.FloatField(null=True, default=0)
    sugar_after_min = models.FloatField(null=True, default=0)
    systolic_max = models.IntegerField(null=True, default=0)
    systolic_min = models.IntegerField(null=True, default=0)
    diastolic_max = models.IntegerField(null=True, default=0)
    diastolic_min = models.IntegerField(null=True, default=0)
    pulse_max = models.IntegerField(null=True, default=0)
    pulse_min = models.IntegerField(null=True, default=0)
    weight_max = models.FloatField(null=True, default=0)
    weight_min = models.FloatField(null=True, default=0)
    bmi_max = models.FloatField(null=True, default=0)
    bmi_min = models.FloatField(null=True, default=0)
    body_fat_max = models.FloatField(null=True, default=0)
    body_fat_min = models.FloatField(null=True, default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))

# 個人設定
class setting_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    after_recording = models.IntegerField(null=True, default=0)
    no_recording_for_a_day = models.IntegerField(null=True, default=0)
    over_max_or_under_min = models.IntegerField(null=True, default=0)
    after_meal = models.IntegerField(null=True, default=0)
    unit_of_sugar = models.IntegerField(null=True, default=0)
    unit_of_weight = models.IntegerField(null=True, default=0)
    unit_of_height = models.IntegerField(null=True, default=0)
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# vip
class vip_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    level = models.IntegerField(null=True, default=0)
    remark = models.FloatField(null=True, default=0)
    started_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    ended_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    updated_at = models.DateTimeField(default= datetime.datetime.now().strftime("%Y-%m-%d %H"))

# 血壓
class blood_pressure_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    systolic = models.IntegerField(null=True, default=0)
    diastolic = models.IntegerField(null=True, default=0)
    pulse = models.IntegerField(null=True, default=0)
    recorded_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))

# 血糖
class blood_sugar_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    sugar = models.FloatField(null=True, default=0)
    timeperiod = models.IntegerField(null=True, default=0)
    drug = models.IntegerField(null=True, default=0)
    exercise = models.IntegerField(null=True, default=0)
    recorded_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 體重
class body_weight_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    weight = models.FloatField(null=True, default=0)
    body_fat = models.FloatField(null=True, default=0)
    bmi = models.FloatField(null=True, default=0)
    recorded_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))

# 分享
class share_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    row_id = models.IntegerField(null=True, default=0)
    type = models.IntegerField(null=True, default=0)
    relation_type = models.IntegerField(null=True, default=0)

# 飲食日記
class diet_diary_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    description = models.CharField(max_length=255, null=True, default="")
    meal = models.IntegerField(null=True, default=0)
    tag = models.CharField(max_length=255, blank=True, null=True, default="")
    image = models.CharField(max_length=255, blank=True, null=True, default="")
    lat = models.CharField(max_length=255, blank=True, null=True, default="")
    lng = models.CharField(max_length=255, blank=True, null=True, default="")
    recorded_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))

# 關懷資訊
class message_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    member_id = models.IntegerField(null=True, default=0)
    message = models.TextField(null=True, default="")
    reply_id = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))

# 就醫資訊
class medical_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    diabetes_type = models.IntegerField(null=True, default=0)
    oad = models.IntegerField(null=True, default=0)
    insulin = models.IntegerField(null=True, default=0)
    anti_hypertensives = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# a1c
class a1c_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    a1c = models.IntegerField(null=True, default=0)
    recorded_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 藥物資訊
class drug_used_info(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    type = models.IntegerField(null=True, default=0)
    name = models.CharField(max_length=255, null=True, default="")
    recorded_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))

# 好友接受情形
class friends_requests(models.Model):
    user_id = models.IntegerField(null=True, default=0)
    relation_id = models.IntegerField(null=True, default=0)
    name = models.CharField(max_length=255, null=True, default="")
    relation_type = models.IntegerField(null=True, default=0)
    status = models.IntegerField(null=True, default=0)
    read = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))

#最新消息
class new_info(models.Model):
    member_id = models.IntegerField(null=True, default=0)
    group = models.IntegerField(null=True, default=0)
    title = models.CharField(max_length=255, null=True, default="")
    message = models.TextField(null=True, default="")
    pushed_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H"))