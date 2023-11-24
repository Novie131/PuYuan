from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api', include("puyuan_ap.urls")),

    path('api/user', include("ap_user.urls")),

    path('api/friend', include("ap_friend.urls")),

    path('api/share', include("ap_share.urls"))
]
