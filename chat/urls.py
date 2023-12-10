from django.urls import path


from . import views 

urlpatterns = [
    path("<str:room_chat>/",views.chat,name="chat")
]

app_name="chat"
