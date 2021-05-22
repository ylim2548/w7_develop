from django.shortcuts import render, redirect, get_object_or_404
from .models import Albamon
# Create your views here.

def home(request):
    albamon = Albamon.objects.all()
    context = {
        'albamon':albamon
    }
    return render(request, 'home.html', context)

def detail(request, id):
    detail_data = get_object_or_404(Albamon, pk=id)
    context = {
        'name' : detail_data.name,
        'location' : detail_data.location,
        'detail_info' : detail_data.detail_info,
        'pay' : detail_data.pay,
        'work' : detail_data.work,
        'applicant' : detail_data.applicant,
        'id' : id
    }
    return render(request, 'detail.html', context)

def create_page(request):
    return render(request, 'create.html')

def create(request):
    new_data = Albamon()
    new_data.name = request.POST['name']
    new_data.location = request.POST['location']
    new_data.detail_info = request.POST['detail_info']
    new_data.pay = request.POST['pay']
    new_data.work = request.POST['work']
    new_data.save()
    return redirect('home')

def update_page(request, id):
    update_data = get_object_or_404(Albamon, pk=id)
    context = {
        'id': id,
        'name' : update_data.name,
        'location' : update_data.location,
        'detail_info' : update_data.detail_info,
        'pay' : update_data.pay,
        'work' : update_data.work,
        'applicant' : update_data.applicant,
    }
    return render(request, 'update.html',context)

def update(request, id):
    update_data = get_object_or_404(Albamon, pk=id)
    update_data.name = request.POST['name']
    update_data.location = request.POST['location']
    update_data.detail_info = request.POST['detail_info']
    update_data.pay = request.POST['pay']
    update_data.work = request.POST['work']
    update_data.save()
    return redirect('home')
 
def delete(request, id):
    delete_data = get_object_or_404(Albamon, pk=id)
    delete_data.delete()
    return redirect('home')

def plus(request, id):
    data = get_object_or_404(Albamon, pk=id)
    data.applicant += 1
    data.save()
    return redirect('detail', id)

def minus(request, id):
    data = get_object_or_404(Albamon, pk=id)
    data.applicant -= 1
    data.save()
    return redirect('detail', id)
