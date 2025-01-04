from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm
from django.contrib.auth import login

def indexpage(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

def tweet_create(request):
    tweet=None
    if request.method== 'POST':  #user submit form
       form= TweetForm(request.POST,request.FILES)
       if form.is_valid():  #form validate by csrf_token
           tweet=form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

def tweet_edit(request,tweet_id):
    tweet= get_object_or_404(Tweet , pk=tweet_id , user=request.user)

    if request.method =='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)

        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html' , {'form':form})

def tweet_delete(request ,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id , user=request.user)

    if request.method== "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request , 'tweet_delete_confirmation.html' , {'tweet': tweet})

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html' , {'form':form})
