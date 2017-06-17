from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import ExtendGroup, UserDetails, Chats


@login_required
def home(request, group_id):
    group_obj = ExtendGroup.objects.get(id=group_id)
    try:
        g = group_obj.user_set.get(username=request.user)
        chat = group_obj.chat.all()
        return render(request, 'home.html', {"home":home, "chat":chat, "group_obj":group_obj })

    except:
        return HttpResponse("You are not authorized to access this Group")
    # chat = group_obj.chat.all()
    # return render(request, 'home.html', {"home":home, "chat":chat, "group_obj":group_obj })

def Post(request):
    if request.is_ajax():
        group_id = request.POST["group_id"]
        msg = request.POST["msgbox"]
        group_obj = ExtendGroup.objects.get(id=group_id)
        chats1 = Chats(user=request.user, message=msg)
        chats1.save()
        group_obj.chat.add(chats1)
        return JsonResponse({'msg': msg, 'user':chats1.user.username })

@login_required
def group(request):
    # result = UserDetails.objects.filter(user=request.user)
    # for staff in result:
    #     groups = staff.group.all()

    result = User.objects.filter(username = request.user)
    for staff in result:
        groups = staff.groups.all()

    manage_group = ExtendGroup.objects.all()
    return render(request, 'group.html', {"groups":groups, "manage_group":manage_group})

def Someonetyping(request):
    if request.is_ajax():
        user = request.user

        return JsonResponse({'user':user.username })

def Messages(request, group_id): #extra
    group_obj = ExtendGroup.objects.get(id=group_id)
    chat = group_obj.chat.all()
    return render(request, 'messages.html',{"chat": chat})

def Someone(request):
    user = request.user
    return render(request, 'someone.html',{"user":user})
