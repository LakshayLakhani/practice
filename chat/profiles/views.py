import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext, context
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.template.loader import render_to_string

from accounts.models import ExtendGroup, UserDetails, Chats
from .models import Friendship, Posts
from .froms import UserDetailsForm, PostsForm

@login_required
def profile(request):
    user = request.user
    userdetails_obj = UserDetails.objects.get(user=request.user)
    # user_status = Posts.objects.filter(user=request.user).order_by('-created')
    user_status = Posts.objects.filter(Q(user=request.user) | Q(to_friend_wall=request.user)).order_by('-created')

    if len(user_status) > 10:
        user_status = user_status[:10]
        more = True
    else:
        more = False

    # result = User.objects.filter(username=request.user)
    result = User.objects.get(username=request.user)

    friend_set = user.friend_set.all()
    values = friend_set.values("to_friend")
    following_length = len(values)
    friends_list = []
    for i in range(0, following_length):
       for key, value in values[i].iteritems():
            friends_list.append(value)

    following = User.objects.filter(id__in=friends_list)

    to_friend_set = user.to_friend_set.all()
    values_from = to_friend_set.values("from_friend_id")
    followers_length = len(values_from)
    followers_list = []
    for i in range(0, followers_length ):
        for key, value in values_from[i].iteritems():
            followers_list.append(value)

    followers = User.objects.filter(id__in=followers_list)

    # for staff in result:
    #     groups = staff.groups.all()

    groups = result.groups.all()

    if request.method == 'POST':
        form = UserDetailsForm(request.POST or None, request.FILES, instance=userdetails_obj)

        if form.is_valid():
            cd = form.cleaned_data
            userdetail = UserDetails.objects.get(user=request.user)
            userdetail.user_description = cd["user_description"]
            userdetail.state = cd["state"]
            userdetail.city = cd["city"]
            # userdetail.city = cd["city"]
            userdetail.mobile_no = cd["mobile_no"]
            userdetail.address = cd["address"]
            # userdetail = UserDetails.objects.create(user_description=cd["user_description"],
            #     state=cd["state"], city=cd["city"], mobile_no=cd["mobile_no"], address=cd["address"],
            #     )

            #
            # candidate = form.save(commit=False)
            # candidate.contact_no = form.cleaned_data['contact_no']
            # candidate.save()

            # return redirect('show_candidate', candidate_id=candidate.id)

            if request.FILES:
                userdetail.image = request.FILES.get("image")
            userdetail.save()
            print userdetail.image
            return redirect('profile')

    else:
        form = UserDetailsForm(instance=userdetails_obj)

    return render(request, 'profile.html', {"userdetails_obj": userdetails_obj,
        "form":form, "user_status":user_status, "groups":groups,
        "following":following, "following_length":following_length,
        "followers_list":followers_list, "followers_length":followers_length,
        "followers":followers, "start":10, "more":more,
    })


def friends_profile(request, id):

    userdetails_obj = UserDetails.objects.get(id=id)
    searched_user = User.objects.get(id=id)
    # user_status = Posts.objects.filter(user_id=id,).order_by('-created')
    user_status = Posts.objects.filter(Q(user_id=id) | Q(to_friend_wall=searched_user)).order_by('-created')
    user = request.user
    # searched_user = User.objects.get(id=id)

    if len(user_status) > 10:
        user_status = user_status[:10]
        more = True
    else:
        more = False


    if user == searched_user :
        return redirect("profile")

    else:
        # user = User.objects.get(id=id)
        friend = user.friend_set.all()
        friend_values = friend.values("to_friend")
        length = len(friend_values)
        if_following = []
        for i in range(0, length):
           for key, value in friend_values[i].iteritems():
                if_following.append(value)

        friend_set = searched_user.friend_set.all()
        values = friend_set.values("to_friend")
        following_length = len(values)
        friends_list = []
        for i in range(0, following_length):
            for key, value in values[i].iteritems():
                friends_list.append(value)

        following = User.objects.filter(id__in=friends_list)

        to_friend_set = searched_user.to_friend_set.all()
        values_from = to_friend_set.values("from_friend_id")
        followers_length = len(values_from)
        followers_list = []
        for i in range(0, followers_length ):
            for key, value in values_from[i].iteritems():
                followers_list.append(value)

        followers = User.objects.filter(id__in=followers_list)

    return render(request, 'profile.html', {"userdetails_obj": userdetails_obj,
        "friend_set":friend_set, "if_following":if_following,
        "user_status":user_status, "following":following, "followers":followers,
        "following_length":following_length, "followers_length":followers_length,
        "searched_user":searched_user
        })


def add_friends(request, id):
    response = {"status": False, "errors": []}
    if request.is_ajax() and request.POST['action'] == "follow" :
        friend = get_object_or_404(User, id=id)
        friendship = Friendship( from_friend=request.user, to_friend=friend)
        friendship.save()
        response["status"] = True
        return HttpResponse(json.dumps(response))

    if request.is_ajax() and request.POST['action'] == "unfollow" :
        friend = get_object_or_404(User, id=id)
        friendship = Friendship.objects.get(from_friend=request.user, to_friend=friend)
        friendship.delete()
        response["status"] = True
        return HttpResponse(json.dumps(response))

def mainhome(request):
    result = User.objects.get(username=request.user)
    groups = result.groups.all()
    userdetails_obj = UserDetails.objects.get(user=request.user)
    user = request.user
    user_id = request.user.id
    friend_set = user.friend_set.all()
    values = friend_set.values("to_friend")
    length = len(values)
    friends_list = []
    for i in range(0, length):
       for key, value in values[i].iteritems():
            friends_list.append(value)

    friends_list.append(user_id)

    friends = User.objects.filter(id__in = friends_list)
    # post = Posts.objects.filter(Q(user_id__in = friends_list) | Q(to_friend_wall__in = friends)).order_by('-created')
    # post = Posts.objects.filter(to_friend_wall__in = friends).order_by('-created')
    post = Posts.objects.filter(user_id__in = friends_list).order_by('-created')

    if len(post) > 10:
        post = post[:10]
        more = True
    else:
        more = False

    # if request.method == 'POST':
    #     form = PostsForm(request.POST or None, request.FILES, instance=userdetails_obj)
    #
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         post = Posts.objects.get(user=user)
    #         post.status = cd["status"]
    #
    #         if request.FILES:
    #             post.image = request.FILES.get("image")
    #         post.save()
    #         print post.image

    # else:
    form = PostsForm()

    return render(request, "home_page.html", {"user":user, "post":post,
        "userdetails_obj":userdetails_obj, "groups":groups, "more":more,
        "start":10, "form":form
        })


def post(request):
    response = {"status": False, "errors": []}

    if request.is_ajax() and request.POST["for"] == "posting_on_ourself_wall":

        # if request.method == 'POST':
        #     form = PostsForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         print "yes"
        #         status = form.cleaned_data["status"]
        #         print status
        #

        status = request.POST["post"]
        image = request.POST.get("image")
        print image
        post = Posts.objects.create(user=request.user, status=status, image=image)

        print post.image
                # post.status = cd["status"]


        # status = request.POST["post"]
        # post = Posts.objects.create(user=request.user, status=status)
        # post = get_object_or_404(Posts, user=request.user)
        # post.status = status
        # post.save()
        # print post.status
        response["post"] = post.status
        response["post_user_first_name"] = post.user.first_name
        response["post_user_last_name"] = post.user.last_name
        response["status"] = True
        return HttpResponse(json.dumps(response))

    if request.is_ajax() and request.POST["for"] == "posting_on_friends_wall":
        status = request.POST["post"]
        friend_id = request.POST["friend_id"]
        friend = User.objects.get(id=friend_id)
        post = Posts.objects.create(user=request.user, status=status, to_friend_wall=friend )
        # post.to_friend_wall = user.friend_id
        # post.save()
        response["post"] = post.status
        response["post_user_first_name"] = post.user.first_name
        response["post_user_last_name"] = post.user.last_name
        response["post_to_friend_wall_frist_name"] = post.to_friend_wall.first_name
        response["post_to_friend_wall_last_name"] = post.to_friend_wall.last_name
        response["post_user_id"] = post.user.id
        response["post_to_friend_wall_id"] = post.to_friend_wall.id
        response["status"] = True
        return HttpResponse(json.dumps(response))


# def posts(request):
#     # user = request.user
#     if request.method == 'POST':
#         form = PostsForm(request.POST or None, request.FILES)
#
#         if form.is_valid():
#             cd = form.cleaned_data
#             post = Posts.objects.get(user=request.user)
#             if request.FILES:
#                 post.image = request.FILES.get("image")
#             post.status = cd["status"]
#             post.save()

            # userdetail.user_description = cd["user_description"]
            # userdetail.state = cd["state"]
            # userdetail.city = cd["city"]
            # userdetail.city = cd["city"]
            # userdetail.mobile_no = cd["mobile_no"]
            # userdetail.address = cd["address"]
            # userdetail = UserDetails.objects.create(user_description=cd["user_description"],
            #     state=cd["state"], city=cd["city"], mobile_no=cd["mobile_no"], address=cd["address"],
            #     )

            #
            # candidate = form.save(commit=False)
            # candidate.contact_no = form.cleaned_data['contact_no']
            # candidate.save()

            # return redirect('show_candidate', candidate_id=candidate.id)

            # if request.FILES:
            #     userdetail.image = request.FILES.get("image")
            # userdetail.save()
            # return redirect('profile')

    # else:
    #     form = PostsForm()
    #
    # return render(request, 'profile.html', {"userdetails_obj": userdetails_obj,})

def load_more_user(request):
    print "in_load_more"
    start = int(request.POST.get('start'))
    user_status = Posts.objects.filter(Q(user=request.user) | Q(to_friend_wall=request.user)).order_by('-created')
    if len(user_status) > start+10:
        user_status = user_status[start:start+10]
        more = True
    else:
        user_status = user_status[start:]
        more = False

    context = {"user_status": user_status,}

    template = render_to_string("load_more_user.html", context, context_instance=RequestContext(request))

    response = {"start": start+10, "more": more, "data": template}

    return HttpResponse(json.dumps(response), content_type="applicaton/json")

def home_load_more_user(request):
    print "in_home_load_more"
    user = request.user
    user_id = request.user.id
    friend_set = user.friend_set.all()
    values = friend_set.values("to_friend")
    length = len(values)
    friends_list = []
    for i in range(0, length):
       for key, value in values[i].iteritems():
            friends_list.append(value)

    friends_list.append(user_id)

    start = int(request.POST.get('start'))
    user_posts = Posts.objects.filter(user_id__in = friends_list).order_by('-created')
    # user_status = Posts.objects.filter(Q(user=request.user) | Q(to_friend_wall=request.user)).order_by('-created')
    if len(user_posts) > start+10:
        user_posts = user_posts[start:start+10]
        more = True
    else:
        user_posts = user_posts[start:]
        more = False

    context = {"user_posts": user_posts,}

    template = render_to_string("home_load_more_user.html", context, context_instance=RequestContext(request))

    response = {"start": start+10, "more": more, "data": template}

    return HttpResponse(json.dumps(response), content_type="applicaton/json")

def searching_friend(request):
    if request.is_ajax():
        search = request.GET.get('q', '')
        fetch_friends = User.objects.filter(Q(first_name__icontains=search) |
            Q(last_name__icontains=search) | Q(username=search))
        response_data = []

        for fetch_friend in fetch_friends:
            response_data.append(fetch_friend.user.first_name)

        data = json.dumps(response_data)

    else:
        data = "fail"

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

    # return HttpResponse("lakshay")
