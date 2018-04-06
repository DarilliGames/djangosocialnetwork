from chatroom.models import *


def count_unread_mail(request):
    if request.user.is_anonymous():
        return {'unread_mail': 0, 'unseen_messages': 0, 'totalnotification': 0}  
    else:
        unread = request.user.messages_received.filter(read=False)
        cauthor = PrivateChat.objects.filter(creator=request.user, creatorread=False)
        callowed = PrivateChat.objects.filter(allowed=request.user, allowedread=False)
        
        
        
        return { 'unread':unread, 'unread_mail' : len(unread), 'totalnotification': len(unread)+len(cauthor)+len(callowed), 'cauthor':cauthor, 'callowed':callowed }