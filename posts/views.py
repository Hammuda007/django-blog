from django.shortcuts import render
from.models import Post
from.forms import PostForm

# Create your views here.


def post_list(request):
    all=Post.objects.all()
    return render(request,'posts.html',{'data':all})





def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'single.html',{'data':post})


def create_post(request):
    if request.method=='POST':
        print('in post ....')
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        print('in get ...')
        form=PostForm()
    return render(request,'create.html',{'form':form})

