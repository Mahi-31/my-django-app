# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    members_list = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'all_members': members_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    print(mymember)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'allmembers': mydata,
    }
    return HttpResponse(template.render(context, request))

