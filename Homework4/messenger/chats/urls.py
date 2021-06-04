from django.urls import path
from chats.views import chatList, chatDetail, chatCreate

urlpatterns = [
    path('', chatList, name='chatList'),
    path('<chat_id>/', chatDetail, name='chatDetail'),
    path('new_chat/<chat_id>/', chatCreate, name='chatCreate'),
]