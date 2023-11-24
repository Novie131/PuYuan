from django.shortcuts import render
from puyuan_ap.models import *
from django.http import JsonResponse
from django.contrib.sessions.models import Session
import json

# Create your views here.
# 分享
def share(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        token = request.headers.get('Authorization').split()[1]
        share_info.objects.create(
            user_id=Session.objects.filter(session_key=token)[0].get_decoded()['id'],
            type=data["type"],
            row_id=data["id"],
            relation_type=data["relation_type"]
        )
        output = {"status": "0", "message": "成功"}
        return JsonResponse(output, safe=False)
    
# 查看分享
def get_share(request, type):
    if request.method == "GET":
        output = {
            "status": "0",
            "message": "成功",
            "records": []
        }
        get_share_data = share_info.objects.filter(
            relation_type=request.get_full_path().split("/")[3]
        ).values()
        for row in get_share_data:
            if row["type"] == 0:
                get_data = blood_pressure_info.objects.filter(id=row["row_id"]).values()
                get_user_data = register_info.objects.filter(id=get_data[0]['user_id']).values()[0]
                for data in get_data:
                    output["records"].append(
                        {
                            "id": data["id"],
                            "user_id": data["user_id"],
                            "systolic": data["systolic"],
                            "diastolic": data["diastolic"],
                            "pulse": data["pulse"],
                            "created_at": datetime.strftime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
                            "recorded_at": datetime.strftime(data["recorded_at"], "%Y-%m-%d %H:%M:%S"),
                            "type": 0,
                            "relation_type": row["relation_type"],
                            "relation_id": 1,
                            
                            "weight": 0,
                            "body_fat": 0,
                            "bmi": 0,
                            "sugar": 0, 
                            "exercise": 0,
                            "drug": 0,
                            "timeperiod": 0,
                            "description": "",
                            "meal": 0,
                            "tag": [[""]],
                            "url": "https://hackmd.io/_uploads/rJzUgN5jh.png",
                            "message": "",
                            "image": [""],
                            "location": {
                                "lat": "",
                                "lng": ""
                            },
                            "reply": "",
                            "user":{
                                "id": get_user_data["id"],
                                "name": get_user_data["name"],
                                "account": get_user_data["account"],
                                "email": get_user_data["email"],
                                "phone": get_user_data["phone"],
                                "fb_id": "fb_" + str(get_user_data["id"]),
                                "status": get_user_data["status"],
                                "group": get_user_data["group"],
                                "birthday": datetime.strftime(get_user_data["birthday"], "%Y-%m-%d"),
                                "height": get_user_data["height"],
                                "gender": get_user_data["gender"],
                                "unread_records": [0, 0, 0],
                                "verified": get_user_data["state"],
                                "privacy_policy": 1,
                                "must_change_password": get_user_data["must_change_password"],
                                "badge": get_user_data["badge"],
                                "created_at": datetime.strftime(get_user_data["created_at"], "%Y-%m-%d %H:%M:%S"),
                                "updated_at": datetime.strftime(get_user_data["updated_at"], "%Y-%m-%d %H:%M:%S")
                            }
                        }
                    )
            elif row["type"] == 1:
                get_data = body_weight_info.objects.filter(id=row["row_id"]).values()
                get_user_data = register_info.objects.filter(id=get_data[0]['user_id']).values()[0]
                for data in get_data:
                    output["records"].append(
                        {
                            "id": data["id"],
                            "user_id": data["user_id"],
                            "weight": data["weight"],
                            "body_fat": data["body_fat"],
                            "bmi": data["bmi"],
                            "created_at": datetime.strftime(data["recorded_at"], "%Y-%m-%d %H:%M:%S"),
                            "recorded_at": datetime.strftime(data["recorded_at"], "%Y-%m-%d %H:%M:%S"),
                            "type": 1,
                            "relation_type": row["relation_type"],
                            "relation_id": 1,
                            
                            "systolic": 0,
                            "diastolic": 0,
                            "pulse": 0,
                            "sugar": 0, 
                            "exercise": 0,
                            "drug": 0,
                            "timeperiod": 0,
                            "description": "",
                            "meal": 0,
                            "tag": [['']],
                            "url": "https://hackmd.io/_uploads/rJzUgN5jh.png",
                            "message": "",
                            "image": [""],
                            "location": {
                                "lat": "",
                                "lng": ""
                            },
                            "reply": "",
                            "user":{
                                "id": get_user_data["id"],
                                "name": get_user_data["name"],
                                "account": get_user_data["account"],
                                "email": get_user_data["email"],
                                "phone": get_user_data["phone"],
                                "fb_id": "fb_" + str(get_user_data["id"]),
                                "status": get_user_data["status"],
                                "group": get_user_data["group"],
                                "birthday": datetime.strftime(get_user_data["birthday"], "%Y-%m-%d"),
                                "height": get_user_data["height"],
                                "gender": get_user_data["gender"],
                                "unread_records": [0, 0, 0],
                                "verified": get_user_data["state"],
                                "privacy_policy": 1,
                                "must_change_password": get_user_data["must_change_password"],
                                "badge": get_user_data["badge"],
                                "created_at": datetime.strftime(get_user_data["created_at"], "%Y-%m-%d %H:%M:%S"),
                                "updated_at": datetime.strftime(get_user_data["updated_at"], "%Y-%m-%d %H:%M:%S")
                            }
                        }
                    )
            elif row["type"] == 2:
                get_data = blood_sugar_info.objects.filter(id=row["row_id"]).values()
                
                get_user_data = register_info.objects.filter(id=get_data[0]['user_id']).values()[0]
                for data in get_data:
                    output["records"].append(
                        {
                            "id": data["id"],
                            "user_id": data["user_id"],
                            "sugar": data["sugar"],
                            "exercise": data["exercise"],
                            "drug": data["drug"],
                            "timeperiod": data["timeperiod"],
                            "created_at": datetime.strftime(data["recorded_at"], "%Y-%m-%d %H:%M:%S"),
                            "recorded_at": datetime.strftime(data["recorded_at"], "%Y-%m-%d %H:%M:%S"),
                            "type": 2,
                            "relation_type": row["relation_type"],
                            "relation_id": 1,
                            
                            "systolic": 0,
                            "diastolic": 0,
                            "pulse": 0,
                            
                            "weight": 0,
                            "body_fat": 0,
                            "bmi": 0,
                            "description": "",
                            "meal": 0,
                            "tag": [[""]],
                            "url": "https://hackmd.io/_uploads/rJzUgN5jh.png",
                            "message": "",
                            "image": [""],
                            "location": {
                                "lat": "",
                                "lng": ""
                            },
                            "reply": "",
                            "user": {
                                "id": get_user_data["id"],
                                "name": get_user_data["name"],
                                "account": get_user_data["account"],
                                "email": get_user_data["email"],
                                "phone": get_user_data["phone"],
                                "fb_id": "fb_" + str(get_user_data["id"]),
                                "status": get_user_data["status"],
                                "group": get_user_data["group"],
                                "birthday": datetime.strftime(get_user_data["birthday"], "%Y-%m-%d"),
                                "height": get_user_data["height"],
                                "gender": get_user_data["gender"],
                                "unread_records": [0, 0, 0],
                                "verified": get_user_data["state"],
                                "privacy_policy": 1,
                                "must_change_password": get_user_data["must_change_password"],
                                "badge": get_user_data["badge"],
                                "created_at": datetime.strftime(get_user_data["created_at"], "%Y-%m-%d %H:%M:%S"),
                                "updated_at": datetime.strftime(get_user_data["updated_at"], "%Y-%m-%d %H:%M:%S")
                            }
                        }
                    )
            elif row["type"] == 3:
                get_data = diet_diary_info.objects.filter(id=row["row_id"]).values()
                get_user_data = register_info.objects.filter(id=get_data[0]['user_id']).values()[0]
                for data in get_data:
                    output["records"].append(
                        {
                            "id": data["id"],
                            "user_id": data["user_id"],
                            "description": data["description"],
                            "meal": get_data["meal"],
                            "drug": get_data["drug"],
                            "tag": json.loads(data["tag"]),
                            "url": "https://hackmd.io/_uploads/rJzUgN5jh.png",
                            "message": "",
                            "image": list(data["image"]),
                            "location": {
                                "lat": str(data["lat"]),
                                "lng": str(data["lng"])
                            },
                            "reply": "",
                            "created_at": datetime.strftime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
                            "recorded_at": datetime.strftime(data["recorded_at"], "%Y-%m-%d %H:%M:%S"),
                            "type": 3,
                            "relation_type": row["relation_type"],
                            "relation_id": 1,
                            
                            "systolic": 0,
                            "diastolic": 0,
                            "pulse": 0,
                            "weight": 0,
                            "body_fat": 0,
                            "bmi": 0,
                            "sugar": 0, 
                            "exercise": 0,
                            "drug": 0,
                            "timeperiod": 0,
                            "user":{
                                "id": get_user_data["id"],
                                "name": get_user_data["name"],
                                "account": get_user_data["account"],
                                "email": get_user_data["email"],
                                "phone": get_user_data["phone"],
                                "fb_id": "fb_" + str(get_user_data["id"]),
                                "status": get_user_data["status"],
                                "group": get_user_data["group"],
                                "birthday": datetime.strftime(get_user_data["birthday"], "%Y-%m-%d"),
                                "height": get_user_data["height"],
                                "gender": get_user_data["gender"],
                                "unread_records": [0, 0, 0],
                                "verified": get_user_data["state"],
                                "privacy_policy": 1,
                                "must_change_password": get_user_data["must_change_password"],
                                "badge": get_user_data["badge"],
                                "created_at": datetime.strftime(get_user_data["created_at"], "%Y-%m-%d %H:%M:%S"),
                                "updated_at": datetime.strftime(get_user_data["updated_at"], "%Y-%m-%d %H:%M:%S")
                            }
                        }
                )
    return JsonResponse(output, safe=False)