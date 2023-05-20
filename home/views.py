from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.contrib import messages
from . import forms
# Create your views here.


def home(request):
    all = models.Todo.objects.all()
    context = {'all': all}
    return render(request, 'home/home.html', context=context)


def detail(request, todo_id):
    todo = models.Todo.objects.get(id=todo_id)
    context = {'todo': todo}
    return render(request, 'home/detail.html', context=context)


def delete(request, todo_id):
    todo = models.Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, f"{todo.title} deleted successfully", extra_tags='success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = forms.TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            models.Todo.objects.create(
                title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(
                request, f"todo {cd['title']} created successfully", extra_tags='success')
            return redirect('home')
    else:
        form = forms.TodoCreateForm()
    return render(request, 'home/create.html', context={'form': form})


def update(request, todo_id):
    todo = models.Todo.objects.get(id=todo_id)

    if request.method == 'POST':
        form = forms.TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"your f{todo.title} updated successfully", extra_tags='success')
            return redirect('detail', todo_id)
    else:
        form = forms.TodoUpdateForm(instance=todo)

    return render(request, 'home/update.html', context={'form': form})
