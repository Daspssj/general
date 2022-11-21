from django.shortcuts import render, redirect,get_object_or_404
from  .models import Post, comentario
from .forms import  NewRegister,CommentForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect

def dashboard(request):
    return render (request,'dashboard.html')

def inicio(request):
    return render (request, 'inicio.html')


def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = NewRegister()
    return render(request, 'registration/register.html', {'form':form})


def comentar(request,pk):
    coment = comentario.objects.get(id=pk)
    tienelike = request.user in comentario.likes.all()
    return render(request, 'post_detail.html', {'coment': coment, 'likes':coment.cantidad_likes(), 'tienelike': tienelike})

def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)
    comentarios = post.comentarios.filter(active=True)
    
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect("")
    else:
        form = CommentForm

    return render(request, 'post_detail.html',{'post':post, 'comentarios':comentarios,'form':form,})

def darlike(request, pk):
    post = get_object_or_404(comentario, id=pk)
    if request.user in comentario.likes.all():
        post.likes.remove(request.user)
    else: 
        post.likes.add(request.user)
    return redirect('/comentario/'+ str(comentario.id))








# Create your views here.
