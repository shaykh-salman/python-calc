import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


def calculate(text_data):
    num1 = int(text_data['num1']);
    num2 = int(text_data['num2']);
    operator = text_data['operator'];
    if (operator == '+'):
        result = num1 + num2;
    if (operator == '-'):
        result = num1 - num2;
    if (operator == '*'):
        result = num1 * num2;
    if (operator == '/'):
        result = num1 / num2;
    return str(result);


class LogsConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("logs", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("logs", self.channel_name)
        pass

    def receive(self, text_data):
        print('Message Received')
        text_data = json.loads(text_data);
        num1 = text_data['num1'];
        num2 = text_data['num2'];
        operator = text_data['operator'];
        async_to_sync(self.channel_layer.group_send)(
            "logs",
            {
                "type": "logs.message",
                "text": num1 + operator + num2 + ' = ' + calculate(text_data),
            },
        )

    def logs_message(self, event):
        self.send(text_data=event["text"])
