from django.shortcuts import render,redirect,get_object_or_404
from .models import Products
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import CommentForm
from .models import Comment


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def home(request):
	return render(request,'owner/index.html')

def products(request):
	products=Products.objects.all()
	return render(request,'owner/products.html',{'products':products})
def signupuser(request):
	if request.method=='GET':
		return render(request,'owner/signupuser.html',{'form':UserCreationForm()})
	else:
		if request.POST['password1']==request.POST['password2']:
			try:
				user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('loginuser')
			except IntegrityError:
				return render(request,'owner/signupuser.html',{'form':UserCreationForm()},{'error':'username already taken'})
		    	

		    
			
		else:
			return render(request,'owner/signupuser.html',{'form':UserCreationForm()},{'error':'password or username didnot match'})

def logoutuser(request):
	if request.method=='POST':
		logout(request)
		return redirect("home")
def loginuser(request):
	if request.method=='GET':
		return render(request,'owner/loginuser.html',{'form':AuthenticationForm()})
	else:
		username = request.POST['username']
		password=request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is None:
			return render(request,'owner/loginuser.html',{'form':AuthenticationForm()},{'error':'username not found'})
		else:
			login(request,user)
			return redirect("products")
def add_comment_to_post(request, pk):
    post = get_object_or_404(Products,pk=pk)
    #if form.is_valid():
    if request=="POST":
    	comment = form.save(commit=False)
    	comment.save()
    	comment=post.objects.all()
    	return render(request,'owner/post_detail.html',{'product':comment})

            #return redirect('post_detail',pk=post.pk)
            
    else:
    	form = CommentForm()
    	return redirect("products")
    
    return render(request, 'owner/add_comment_to_post.html', {'form':form})

def post_detail(request,val):
	#post = get_object_or_404(Comment,pk=val)
	products=Products.objects.all()
	#products=Products.objects.all()
	#post_detail=Comment.objects.all()
	return render(request,'owner/post_detail.html',{'products':products})




