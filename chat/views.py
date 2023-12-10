from django.shortcuts import render

def chat(request, room_chat):
   context = {
      "room_chat" : room_chat
   }
   return render(request, "chat/chat.html", context) 
