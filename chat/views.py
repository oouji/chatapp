from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    #Home画面を表示するビュー
    template_name = 'home.html'    #HomeというViewクラスではtemplatesフォルダ内のhtmlファイルを使用するということ

class ChatRoom(TemplateView):
    #ChatRoomを表示するビュー
    template_name = 'chat/chat_box.html'   #tempatesフォルダ内のchatフォルダの中のchat_box.htmlを使用