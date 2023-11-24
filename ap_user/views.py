from django.shortcuts import render
from puyuan_ap.models import *
from django.http import JsonResponse
from datetime import datetime
from django.contrib.sessions.models import Session
import json
# Create your views here.

# 2-1 個人資訊設定 & 個人資訊
def user(request):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要

        for obj in data:
            if data[obj] == '':
                continue
            else:
                register_info.objects.filter(id=id).update(**{obj: data[obj]})
        output = {"status": "0", "message": "成功"}
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        user = register_info.objects.filter(id=id).values()[0]
        default = default_info.objects.filter(id=id).values()[0]
        setting = setting_info.objects.filter(id=id).values()[0]
        vip = vip_info.objects.filter(id=id).values()[0]
        output = {
            "status": "0", 
            "message": "成功",
            "user": {
                "id": user['id'],
                "name": user['name'],
                "account": user['account'],
                "email": user['email'],
                "phone": user['phone'],
                "fb_id": "未設置",
                "status": user['status'],
                "group": user['group'],
                "birthday": user['birthday'],
                "height": user['height'],
                "weight": user['weight'],
                "gender": user['gender'],
                "address": user['address'],
                "unread_records": [ 
                    0,
                    0,
                    0
                ],
                "verified": user['state'],
                "created_at": user['created_at'],
                "privacy_policy": user['privacy_policy'],
                "must_change_password": user['must_change_password'],
                "fcm_id": user['fcm_id'],
                "updated_at": user['updated_at'].strftime("%Y-%m-%d %H:%M:%S"),
                "created_at": user['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                "login_times": user['login_times'],
                "default": {
                    "id": default['id'],
                    "user_id": default['user_id'],
                    "sugar_delta_max": default['sugar_delta_max'],
                    "sugar_delta_min": default['sugar_delta_min'],
                    "sugar_morning_max": default['sugar_morning_max'],
                    "sugar_morning_min": default['sugar_morning_min'],
                    "sugar_evening_max": default['sugar_evening_max'],
                    "sugar_evening_min": default['sugar_evening_min'],
                    "sugar_before_max": default['sugar_before_max'],
                    "sugar_before_min": default['sugar_before_min'],
                    "sugar_after_max": default['sugar_after_max'],
                    "sugar_after_min": default['sugar_after_min'],
                    "systolic_max": default['systolic_max'],
                    "systolic_min": default['systolic_min'],
                    "diastolic_max": default['diastolic_max'],
                    "diastolic_min": default['diastolic_min'],
                    "pulse_max": default['pulse_max'],
                    "pulse_min": default['pulse_min'],
                    "weight_max": default['weight_max'],
                    "weight_min": default['weight_min'],
                    "bmi_max": default['bmi_max'],
                    "bmi_min": default['bmi_min'],
                    "body_fat_max": default['body_fat_max'],
                    "body_fat_min": default['body_fat_min'],
                    "created_at": default['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": default['updated_at'].strftime("%Y-%m-%d %H:%M:%S"),
                },
                "setting": {
                    "id": setting['id'],
                    "user_id": setting['user_id'],
                    "after_recording": setting['after_recording'],
                    "no_recording_for_a_day": setting['no_recording_for_a_day'],
                    "over_max_or_under_min": setting['over_max_or_under_min'],
                    "after_meal": setting['after_meal'],
                    "unit_of_sugar": setting['unit_of_sugar'],
                    "unit_of_weight": setting['unit_of_weight'],
                    "unit_of_height": setting['unit_of_height'],
                    "created_at": setting['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": setting['updated_at'].strftime("%Y-%m-%d %H:%M:%S"),
                },
                "vip":{
                    "id": vip['id'],
                    "user_id": vip['user_id'],
                    "level": vip['level'],
                    "remark": vip['remark'],
                    "started_at": vip['started_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    "ended_at": vip['ended_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    "created_at": vip['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": vip['updated_at'].strftime("%Y-%m-%d %H:%M:%S"),
                }
            }
        }
    return JsonResponse(output, safe=False)

# 2-2 個人預設值
def user_default(request):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        fields_to_list = ['sugar_delta_max', 'sugar_delta_min',
                          'sugar_morning_max', 'sugar_morning_min', 
                          'sugar_evening_max', 'sugar_evening_min',
                          'sugar_before_max', 'sugar_before_min', 
                          'sugar_after_max', 'sugar_after_min',
                          'systolic_max', 'systolic_min', 
                          'diastolic_max', 'diastolic_min', 
                          'pulse_max', 'pulse_min',
                          'weight_max', 'weight_min', 
                          'bmi_max', 'bmi_min',
                          'body_fat_max', 'body_fat_min']
        
        for field in fields_to_list:
            if field in data:
                default_info.objects.filter(id=id).update(**{field: data[field]})
        return JsonResponse({"status": "0", "message": "成功"})
    
# 2-3 個人設定
def user_setting(request):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        fields_to_list = ['after_recording', 'no_recording_for_a_day',
                          'over_max_or_under_min', 'after_meal',
                          'unit_of_sugar', 'unit_of_weight', 'unit_of_height']
        
        for field in fields_to_list:
            if field in data:
                setting_info.objects.filter(id=id).update(**{field: data[field]})
        return JsonResponse({"status": "0", "message": "成功"})
    
# 2-4 血壓測量結果
def blood_pressure(request):
    if request.method == 'POST':
        session_token = request.headers.get('Authorization').split()[1] #重要
        uid = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        data = json.loads(request.body)
        blood_pressure_info.objects.filter(user_id=uid).create(
            systolic=data['systolic'], 
            diastolic=data['diastolic'], 
            pulse=data['pulse'], 
            recorded_at=data['recorded_at']
        )
        return JsonResponse({"status": "0", "message": "成功", "records": "成功"})

# 2-5 體重測量結果
def body_weight(request):
    if request.method == 'POST':
        session_token = request.headers.get('Authorization').split()[1] #重要
        uid = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        data = json.loads(request.body)
        body_weight_info.objects.create(
            user_id=uid,
            weight=data['weight'], 
            body_fat=data['body_fat'], 
            bmi=data['bmi'], 
            recorded_at=data['recorded_at']
        )
        return JsonResponse({"status": "0", "message": "成功"})

# 2-6 血糖測量結果 
def blood_sugar(request):
    if request.method == 'POST':
        session_token = request.headers.get('Authorization').split()[1] #重要
        uid = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        data = json.loads(request.body)
        blood_sugar_info.objects.create(
            user_id=uid,
            sugar=data['sugar'], 
            timeperiod=data['timeperiod'], 
            drug=data['drug'], 
            exercise=data['exercise'], 
            recorded_at=data['recorded_at']
        )
        return JsonResponse({"status": "0", "message": "成功"})

# 2-7 上一筆紀錄資訊 & 刪除日記記錄
def user_records(request):
    if request.method == 'POST':
        get_id = Session.objects.filter(
            session_key=request.headers.get('Authorization').split(" ")[1]
        )[0].get_decoded()["id"]

        output = {
            "status": "0",
            "message": "成功",
            "blood_sugars": {
                "sugar": 0
            },
            "blood_pressures": {
                "systolic": 0,
                "diastolic": 0,
                "pulse": 0
            },
            "weights": {
                "weight": 0
            }
        }

        data = blood_sugar_info.objects.filter(
            user_id=get_id,
            timeperiod=json.loads(request.body)["diet"]
        ).order_by("-recorded_at").values()
        if len(data) != 0:
            output["blood_sugars"] = {
                "sugar": data[0]["sugar"]
            }

        data = blood_pressure_info.objects.filter(user_id=get_id).order_by("-recorded_at").values()
        if len(data) != 0:
            output["blood_pressures"] = {
                "systolic": data[0]["systolic"],
                "diastolic": data[0]["diastolic"],
                "pulse": data[0]["pulse"]
            }

        data = body_weight_info.objects.filter(user_id=get_id).order_by("-recorded_at").values()
        if len(data) != 0:
            output["weights"] = {
                "weight": data[0]["weight"]
            }
        return JsonResponse(output, safe=False)
    if request.method == 'DELETE':
        data = json.loads(request.body)
        deleteObject = data['deleteObject']
        for list in deleteObject:
            if list == 'blood_sugars':
                for i in deleteObject['blood_sugars']:
                    blood_sugar_info.objects.filter(id=i).delete()
                    share_info.objects.filter(row_id=i).delete()
            elif list == 'blood_pressures':
                for i in deleteObject['blood_pressures']:
                    blood_pressure_info.objects.filter(id=i).delete()
            elif list == 'body_weights':
                for i in deleteObject['body_weights']:
                    body_weight_info.objects.filter(id=i).delete()
            elif list == 'diets':
                for i in deleteObject['diets']:
                    diet_diary_info.objects.filter(id=i).delete()
        return JsonResponse({"status": "0", "message": "成功"})

# 2-8 日記列表
def user_diary(request):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1]  # 重要
        uid = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"]  # 重要
        date = request.GET.get('date')
        usr = register_info.objects.filter(id=uid).values()[0]
        output = {
            "status": "0",
            "message": "成功",
            "diary": []
        }

        bp_obj = blood_pressure_info.objects.filter(user_id=uid, 
                                                    recorded_at__date=date).values()
        if len(bp_obj) != 0:
            for bp_data in bp_obj:
                output["diary"].append({
                    "id": bp_data['id'],
                    "user_id": bp_data['user_id'],
                    "systolic": bp_data['systolic'],
                    "diastolic": bp_data['diastolic'],
                    "pulse": bp_data['pulse'],
                    "weight": 0,
                    "body_fat": 0,
                    "bmi": 0,
                    "sugar": 0.0,
                    "exercise": 0,
                    "drug": 0,
                    "timeperiod": 0,
                    "description": " ",
                    "meal": 0,
                    "tag": [{
                        "name": [''],
                        "message": " "
                    }],
                    "image": [" "],
                    "location":{
                        "lat": " ",
                        "lng": " "
                    },
                    "reply": " ",
                    "recorded_at": datetime.strftime(bp_data['recorded_at'], "%Y-%m-%d %H:%M:%S"),
                    "type": "blood_pressure"
                })

        bs_obj = blood_sugar_info.objects.filter(user_id=uid, 
                                                 recorded_at__date=date).values()
        if len(bs_obj) != 0:
            for bs_data in bs_obj:
                output["diary"].append({
                    "id": bs_data['id'],
                    "user_id": bs_data['user_id'],
                    "systolic": 0,
                    "diastolic": 0,
                    "pulse": 0,
                    "weight": 0,
                    "body_fat": 0,
                    "bmi": 0,
                    "sugar": bs_data['sugar'],
                    "timeperiod": bs_data['timeperiod'],
                    "drug": bs_data['drug'],
                    "exercise": bs_data['exercise'],
                    "description": " ",
                    "meal": 0,
                    "tag": [{
                        "name": [''],
                        "message": " "
                    }],
                    "image": [" "],
                    "location": {
                        "lat": " ",
                        "lng": " "
                    },
                    "reply": " ",
                    "recorded_at": datetime.strftime(bs_data['recorded_at'], "%Y-%m-%d %H:%M:%S"),
                    "type": "blood_sugar"
                })

        bw_obj = body_weight_info.objects.filter(user_id=uid, 
                                                 recorded_at__date=date).values()
        if len(bw_obj) != 0:
            for bw_data in bw_obj:
                output["diary"].append({
                    "id": bw_data['id'],
                    "user_id": bw_data['user_id'],
                    "systolic": 0,
                    "diastolic": 0,
                    "pulse": 0,
                    "weight": int(bw_data['weight']),
                    "body_fat": int(bw_data['body_fat']),
                    "bmi": int(bw_data['bmi']),
                    "sugar": 0.0,
                    "timeperiod": 0,
                    "drug": 0,
                    "exercise": 0,
                    "description": " ",
                    "meal": 0,
                    "tag": [{
                        "name": [''],
                        "message": " "
                    }],
                    "image": [" "],
                    "location": {
                        "lat": " ",
                        "lng": " "
                    },
                    "reply": " ",
                    "recorded_at": datetime.strftime(bw_data['recorded_at'], "%Y-%m-%d %H:%M:%S"),
                    "type": "body_weight"
                })
        
        dd_obj = diet_diary_info.objects.filter(user_id=uid, 
                                                recorded_at__date=date).values()
        if len(dd_obj) != 0:
            for dd_data in dd_obj:
                output["diary"].append({
                    "id": dd_data['id'],
                    "user_id": dd_data['user_id'],
                    "systolic": 0,
                    "diastolic": 0,
                    "pulse": 0,
                    "weight": 0,
                    "body_fat": 0,
                    "bmi": 0,
                    "sugar": 0.0,
                    "timeperiod": 0,
                    "drug": 0,
                    "exercise": 0,
                    "description": dd_data['description'],
                    "meal": dd_data['meal'],
                    "tag": [{
                        "name": [usr['name']],
                        "message": " "
                    }],
                    "image": [dd_data['image']],
                    "location": {
                        "lat": dd_data['lat'],
                        "lng": dd_data['lng']
                    },
                    "reply": " ",
                    "recorded_at": datetime.strftime(dd_data['recorded_at'], "%Y-%m-%d %H:%M:%S"),
                    "type": "diet"
                })
        
        return JsonResponse(output)

# 2-9 飲食日記
def user_diet(request):
    if request.method == 'POST':
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        data = json.loads(request.body)
        tag_data = []
        for msg_obj in tag_data:
            tag_data.append(
                {
                    "name": msg_obj['name'],
                    "message": msg_obj['message']
                }
            )
        tag = str(tag_data)
        diet_diary_info.objects.filter(user_id=id).create( 
            description=data['description'],
            meal=data['meal'], 
            tag=[tag], 
            image=data['image'],
            lat=data['lat'], 
            lng=data['lng'], 
            recorded_at=data['recorded_at']
        )
        return JsonResponse({
            "status": "0", 
            "message": "成功", 
            "image_url": "https://medium.com/%E5%BD%BC%E5%BE%97%E6%BD%98%E7%9A%84-swift-ios-app-%E9%96%8B%E7%99%BC%E6%95%99%E5%AE%A4/playground-%E8%AA%BF%E8%89%B2%E5%8E%BB%E8%83%8C%E5%9C%96%E7%89%87-%E7%9A%AE%E5%8D%A1%E4%B8%98-a1faec0910fd"
        })

# 2-10 糖化血色素
def user_a1c(request):
    if request.method == 'POST':
        get_id = Session.objects.filter(
            session_key=request.headers.get('Authorization').split(" ")[1]
        )[0].get_decoded()['id']
        a1c_info.objects.create(
            user_id=get_id,
            a1c=json.loads(request.body)["a1c"],
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            recorded_at=json.loads(request.body)["recorded_at"]
        )
        output = {"status": "0", "message": "成功"}
    if request.method == 'GET':
        try:
            get_data = a1c_info.objects.filter(
                user_id=Session.objects.filter(
                    session_key=request.headers.get('Authorization').split(" ")[1]
                )[0].get_decoded()['id']
            ).values()
        except IndexError:
            return JsonResponse({"status": "1", "message": "失敗"}, safe=False)
        output = {
            "status": "0",
            "message": "成功",
            "a1cs": []
        }
        for data in get_data:
            output["a1cs"].append({
                "id": data["id"],
                "user_id": data["user_id"],
                "a1c": str(data["a1c"]),
                "recorded_at": datetime.strftime(data["recorded_at"], "%Y-%m-%d %H:%M:%S"),
                "created_at": datetime.strftime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.strftime(data["updated_at"], "%Y-%m-%d %H:%M:%S")
            })
    if request.method == 'DELETE':
        for index in list(json.loads(request.body)["ids[]"]):
            a1c_info.objects.filter(id=index).delete()
            output = {"status": "0", "message": "成功"}
        session_token = request.headers.get('Authorization').split()[1]
        uid = Session.objects.get(session_key=session_token).get_decoded()["id"]
        data = json.loads(request.body)
        ids = data['ids[]']
        if a1c_info.objects.filter(user_id=uid):
            for a1c_data in ids:
                a1c_info.objects.filter(id=a1c_data).delete()
                print(a1c_info.objects.filter(id=a1c_data))
        output = {"status": "0", "message": "成功"}
    return JsonResponse(output, safe=False)

# 2-11 就醫資訊
def medical(request):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1] #重要
        uid = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        medical_obj = medical_info.objects.filter(user_id=uid).values()[0]
        output = {
            "status": "0",
            "message": "成功",
            "medical_info": {
                "id": medical_obj['id'],
                "user_id": medical_obj['user_id'],
                "diabetes_type": medical_obj['diabetes_type'],
                "oad": medical_obj['oad'],
                "insulin": medical_obj['insulin'],
                "anti_hypertensives": medical_obj['anti_hypertensives'],
                "created_at": datetime.strftime(medical_obj['created_at'], "%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.strftime(medical_obj['updated_at'], "%Y-%m-%d %H:%M:%S")
            }
        }
    if request.method == 'PATCH':
        data = json.loads(request.body)
        session_token = request.headers.get('Authorization').split()[1] #重要
        uid = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        for obj in data:
            medical_info.objects.filter(user_id=uid).update(**{obj: int(data[obj])})
            print(medical_info.objects.filter(user_id=uid).update(**{obj: int(data[obj])}))
        output = {"status": "0", "message": "成功"}
    return JsonResponse(output)

# 2-12 藥物資訊
def drug_used(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        drug_type = data['type']
        drug_name = data['name']
        drug_used_info.objects.create(user_id=id, 
                                      type=drug_type, 
                                      name=drug_name, 
                                      recorded_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        output = {"status": "0", "message": "成功"}
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        drug = drug_used_info.objects.filter(user_id=id).values()
        drug_data = []
        for drug_obj in drug:
            drug_data.append(
                {
                    "id": drug_obj['id'],
                    "user_id": drug_obj['user_id'],
                    "type": drug_obj['type'],
                    "name": drug_obj['name'],
                    "recorded_at": drug_obj['recorded_at'],
                }
            )
        if drug_data:
            json_data = {
                "status": "0",
                "message": "成功",
                "drug_useds": drug_data
            }
            output = json_data
        else:
            output = {"status": "1", "message": "失敗"}
    if request.method == 'DELETE':
        session_token = request.headers.get('Authorization').split()[1] #重要
        uid = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        data = json.loads(request.body)
        ids = data['ids[]']
        if drug_used_info.objects.filter(user_id=uid):
            for drug_data in ids:
                drug_used_info.objects.filter(id=drug_data).delete()
        output = {"status": "0", "message": "成功"}
    return JsonResponse(output)

# 2-13 關懷諮詢
def cares(request):
    if request.method == "GET":
        token = request.headers.get('Authorization').split(" ")[1]

        get_id = Session.objects.filter(session_key=token)[0].get_decoded()['id']
        output = {
            "status": "0",
            "message": "成功",
            "cares": []
        }

        get_data = message_info.objects.filter(user_id=get_id).values()
        for data in get_data:
            output["cares"].append({
                "id": data["id"],
                "user_id": get_id,
                "member_id": data["member_id"],
                "reply_id": data["reply_id"],
                "message": data["message"],
                "created_at":  datetime.strftime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.strftime(data["updated_at"], "%Y-%m-%d %H:%M:%S")
            })
        return JsonResponse(output, safe=False)   
    if request.method == 'POST':
        data = json.loads(request.body)
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        message = data['message']
        message_info.objects.filter(user_id=id).create(
            message=message, 
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        output = {"status": "0", "message": "成功"}
        return JsonResponse(output)

# 2-14 更新 badge
def badge(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        session_token = request.headers.get('Authorization').split()[1]
        badge = data['badge']
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"]
        register_info.objects.filter(id=id).update(badge=badge)
        return JsonResponse({"status": "0", "message": "成功"})