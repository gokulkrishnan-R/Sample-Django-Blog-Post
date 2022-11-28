from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,context
from.models import Posts,Comment
from django.views.decorators.csrf import csrf_exempt # Importing this csrf token for excluding some validation 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm
from django.contrib.auth  import authenticate,  login, logout
from django.shortcuts import redirect #,render_to_response
from datetime import datetime

# Create your views here.
def home(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())

@csrf_exempt
def posts(request):
    objects=Posts.objects.all()
    template=loader.get_template("posts.html")
    context={
        "objects":objects,
    }
    """
    comments = Posts.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        new_comment.post = Posts
        new_comment.save()
    else:
        comment_form=new_comment()
    """

    return HttpResponse(template.render(context,request))

def newpost(request):
    template=loader.get_template("newpost.html")
    return HttpResponse(template.render())

@csrf_exempt #without this it's showing csrf token error
def newpostrecord(request):
    post=Posts.objects.all()
    x=request.POST["title"]
    y=request.POST["author"]
    z=request.POST["content"]
    image=request.POST.get("image")
    post=Posts(title=x,author=y,content=z,image=image)
    messages.success(request,"Added Post Successfully!")
    post.save()
    return HttpResponseRedirect(reverse("posts"))

def about(request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render())

def delete(request,id):
    post=Posts.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse("posts"))

def update(request,id):
    myobjects = Posts.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myobjects': myobjects,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt #Excluding this as there is a csrf token error again
def updaterecord(request,id):
    mytitle=request.POST["title"]
    mycontent=request.POST["content"]
    myauthor=request.POST["author"]
    myobj=Posts.objects.get(id=id)
    myobj.title=mytitle
    myobj.content=mycontent
    myobj.author=myauthor
    myobj.save()
    return HttpResponseRedirect(reverse("posts"))

@csrf_exempt
def login_user(request):
    #user_login_datas=Posts.objects.all()
    template=loader.get_template("user_posts.html")
    return HttpResponse(template.render())

#@login_required(login_url = 'login/')
def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name

        user.save()
        return render(request, 'login.html')   
    return render(request, "register.html")

@csrf_exempt    
def Login(request):
    template=loader.get_template("index.html")
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
            #return render_to_response('posts.html', message='Logged In Successfully!')
            #return HttpResponseRedirect(request.META.get("HTTP_REFERER","posts/")) #Redirecting to back page but failed
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'posts.html')   
    return render(request, "login.html")

def Profile(request):
    return render(request, "profile.html")

@csrf_exempt #Excluding this function for CSRF_token validation error 
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs=Posts.objects.filter(title__contains=searched)
        return render(request,"search.html",{"searched":searched,"blogs":blogs})

def Logout(request):
    logout(request)
    #messages.success(request, "Successfully logged out")
    return redirect('/posts/')
    #return render_to_response('posts.html', message='logged-out successfully!')


def user_comments(request,pk):
    comment_object=Posts.objects.get(id=pk)
    form=CommentForm(instance=comment_object)
    if request.method == "POST":
        form=CommentForm(request.POST,instance=comment_object)
        name=request.user.username
        body=form.cleaned_data["comment_body"]
        comments=Comment(user_comments=comment_object,name=name,comment_body=body,posted_on=datetime.now())
        comments.save()
        return redirect("posts")
    else:
        form=CommentForm()

    context={
        "form":form
    }
    return render(request,"user comments.html",context)

"""
def user_comments(request):
    template=loader.get_template("usercomments.html")
    return HttpResponse(template.render())
    """

"""
    mypost=Posts.objects.all()
    template=loader.get_template("user comments.html")
    context={
        "mypost":mypost
    }
    return HttpResponse(template.render(context, request))"""

"""

def add_user_comments(request,id):
    if request.method == "POST":
        commentor_name=request.POST["name"]
        comment_body=request.POST["comment_body"]
        comment_posted_on=request.POST["posted_on"]
        my_comment_objects=Posts.objects.get(id=id)
        my_comment_objects.name=commentor_name
        my_comment_objects.comment_body=comment_body
        my_comment_objects.posted_on=comment_posted_on
        my_comment_objects.save()
    return HttpResponseRedirect(reverse("posts.html"))
"""