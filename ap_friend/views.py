from django.shortcuts import render
from django.http import JsonResponse
from puyuan_ap.models import *
from django.contrib.sessions.models import Session
from django.db.models import Q
import json

# 3-1 獲取控糖團邀請碼
def friend_code(request):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1]  # 重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"]  # 重要
        invite_code = register_info.objects.filter(id=id).values()[0]['invite_code']
        output = {
            "status": "0", 
            "message": "成功", 
            "invite_code": invite_code
        }
        return JsonResponse(output)
    
# 3-2 控糖團列表 (好友列表)
def friends_list(request):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1]  # 重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"]  # 重要
        req = friends_requests.objects.filter(user_id=id).values()
        data_list = {
            "status": "0",
            "message": "成功",
            "friends": []
        }
        for obj in req:
            data_list["friends"].append({
                "id": obj['user_id'],
                "name": obj['name'],
                "relation_type": obj['relation_type'],
            })
        return JsonResponse(data_list)

# 3-3 獲取控糖團邀請  
def friend_requests(request):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1]  # 重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()['id']  # 重要
        usr = register_info.objects.filter(id=id).values()[0]
        req = friends_requests.objects.filter(relation_id=id).values()
        data_list = {
            "status": "0",
            "message": "成功",
            "requests": []
        }
        for obj in req:
            if obj['status'] == 1:
                continue
            else: 
                if obj['status'] == 0:
                    data_list["requests"].append({
                        "id": obj['id'],
                        "user_id": obj['user_id'],
                        "relation_id": obj['relation_id'],
                        "type": obj['relation_type'],
                        "status": obj['status'],
                        "read": obj['read'],
                        "created_at": obj['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                        "updated_at": obj['updated_at'].strftime("%Y-%m-%d %H:%M:%S"),
                        "user": {
                            "id": usr['id'],
                            "name": usr['name'],
                            "account": "fb_" + str(obj["id"]),
                        }
                    })
        return JsonResponse(data_list)

# 3-4 送出控糖團邀請
def friend_send(request):
    if request.method == 'POST':
        session_token = request.headers.get('Authorization').split()[1]  # 重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"]  # 重要
        data = json.loads(request.body)
        friend_type = data['type']
        invite_code = data['invite_code']
        uid = register_info.objects.filter(invite_code=invite_code).values()[0]['id']
        if friends_requests.objects.filter(user_id=uid, status=1):
            return JsonResponse({"status": "2", "message": "已經成為好友了"})
        if register_info.objects.filter(invite_code=invite_code):
            friends_requests.objects.create(user_id=id, 
                                            relation_id=uid,
                                            relation_type=friend_type)
            return JsonResponse({"status": "0", "message": "成功"})
        else:
            return JsonResponse({"status": "1", "message": "邀請碼無效"})

# 3-5 接受控糖團邀請
def invite_accept(request, inviteld):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1]  # 重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"]  # 重要
        inviteld = register_info.objects.filter(id=id).values()[0]['invite_code']
        if register_info.objects.filter(id=id, invite_code=inviteld).exists():
            friends_requests.objects.filter(relation_id=id).update(
                status=1, read=1, 
                updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        return JsonResponse({"status": "0", "message": "成功"})

# 3-6 拒絕控糖團邀請
def invite_refuse(request, inviteld):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1]  # 重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"]  # 重要
        inviteld = register_info.objects.filter(id=id).values()[0]['invite_code']
        if register_info.objects.filter(id=id, invite_code=inviteld).exists():
            friends_requests.objects.filter(relation_id=id).update(
                status=2, read=1, 
                updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        return JsonResponse({"status": "0", "message": "成功"})

# 3-7 刪除更多好友
def invite_remove(request):
    if request.method == "DELETE":
        get_id = Session.objects.filter(
            session_key=request.headers.get('Authorization').split(" ")[1]
        )[0].get_decoded()['id']
        del_id = json.loads(request.body)["ids[]"]
        try:
            friends_requests.objects.filter(
                Q(user_id=get_id, relation_id=del_id) | 
                Q(user_id=del_id, relation_id=get_id)
            ).delete()
            output = {"status": "0", "message": "成功"}
        except:
            output = {"status": "1", "message": "失敗"}
        return JsonResponse(output, safe=False)

# 3-8 控糖團結果
def friend_result(request):
    if request.method == 'GET':
        session_token = request.headers.get('Authorization').split()[1] #重要
        id = Session.objects.filter(session_key=session_token)[0].get_decoded()["id"] #重要
        usr = register_info.objects.filter(id=id).values()[0]
        req = friends_requests.objects.filter(user_id=id).values()
        data_list = {
            "status": "0",
            "message": "成功",
            "results": []
        }
        for obj in req:
            if obj["status"] == 0:
                continue
            else:
                data_list["results"].append({
                    "id": obj['id'],
                    "user_id": obj['user_id'],
                    "relation_id": obj['relation_id'],
                    "type": obj['relation_type'],
                    "status": obj['status'],
                    "read": obj['read'],
                    "created_at": obj['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": obj['updated_at'].strftime("%Y-%m-%d %H:%M:%S"),
                    "relation": {
                        "id": obj['relation_id'],
                        "name": usr['name'],
                        "account": usr['account']
                    }
                })
        return JsonResponse(data_list)






