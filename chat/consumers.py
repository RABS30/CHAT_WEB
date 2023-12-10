from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class chatCosumers(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name          = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name    = "chat_%s" % self.room_name  
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        await self.send(json.dumps({
            "type"      : "connected",
            "message"   : "Anda telah terhubung"
        }))
 
    
    # Menerima pesan yang masuk dari client
    async def receive(self, text_data):
        data = json.loads(text_data)
        
        if data["type"] == "inputMessage" :
            await self.channel_layer.group_send(
                self.room_group_name,
                {   
                "type"      : "chat_message",
                "message"   : data["message"],
                "username"  : data["username"]
                }  
            )
        

    async def chat_message(self, event):
        print(event)
        await self.send(json.dumps({
            "type"      : "inputMessage",
            "message"   : event["message"],
            "username"  : event["username"]
        }))
        

        
    
        
        
    