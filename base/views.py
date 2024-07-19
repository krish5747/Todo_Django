from django.shortcuts import render,redirect
from base.models import student

# Create your views here.
def home(request):
    todos_obj= student.objects.all()
    context={'todos':todos_obj}

    return render(request,"index.html",context)
def fun(request):
    if request.method== "POST":
      name=request.POST.get("name")
      description=request.POST.get("Description")
      status=request.POST.get("status")
      student.objects.create(name=name,description=description,status=status)
      return redirect('home')
    
    return render(request,"create.html")
def edit(request,pk):
  todo_objs=student.objects.get(id=pk)
  context={ 'todos':todo_objs}
  if request.method== "POST":
    todo_objs.name = request.POST.get('name')
    todo_objs.description = request.POST.get('description')
    todo_objs.save()
    return redirect('home')


  return render(request,'edit.html',context)
def delete(request,pk):
  todo_objs =student.objects.get(id=pk)
  todo_objs.delete()
  return redirect('home')

