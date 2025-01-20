from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
       
        savedpost = Post.objects.create(title=title, content=content, author=request.user )
        context = {
            'savedpost': savedpost,
            'posts': posts
        }
    else:
        context = {
            'posts': posts
        }

    return render(request, 'home.html', context)

@login_required
def blogdetail(request,id):
   post=Post.objects.get(id=id)
#    reviews=post.reviews.all()
   if request.method=='POST':
      comment = request.POST.get('comment')
      
      review = Rewive.objects.create(comment=comment, user=user.objects.filter(username=request.user.username).first())
      post.comment.add(review)
   
   return render(request, 'detail.html', {'post': post})
@login_required
def delete_post(request,id):
   post=Post.objects.get(id=id)
   post.delete()
   return redirect('/')

def logout_view(request):  
    logout(request)  
    return redirect('/login') 
   
   

def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confrim_pass=request.POST.get('confirm-password')
        if confrim_pass==password:
            users=user.objects.create(username=username,email=email)
            users.set_password(password)
            users.save()
            return redirect('/login')
        else:
            messages.error(request ,'Password are not same please Try again!')
            return redirect('register_view')
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        users=user.objects.filter(username=username).first()
        if users:
            userauth=authenticate(username=username,password=password)
            if userauth:
                login(request,userauth)
                return redirect('/')
            else:
                messages.error(request,'wrong password!')
        else:
            messages.error(request,'username is not exist!')
    return render(request,'login.html')
@login_required
def profile_page(request):
   profile_user=user.objects.filter(username=request.user.username).first()
   international_dic = {
       'user':profile_user
   }

   return render(request,'profile.html', international_dic)
@login_required
def edit_profile(request):
    current_user = user.objects.get(username=request.user.username)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')  
        if image:
            current_user.image = image
        
        current_user.username = name
        current_user.email = email
        current_user.Bio = bio
        current_user.save()
        return redirect('profile_page')  

    return render(request, 'edit_profile.html', {'user': current_user})
@login_required
def update_post(request,id):
    post =Post.objects.get(id=id)  

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # image = request.FILES.get('image')  
        post.title = title
        post.content = content   
        # if image: 
        #     post.image = image
        
        post.save()  
        return redirect('blogdetail', id=id)

    return render(request, 'update_post.html', {'post': post})