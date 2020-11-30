import csv
import io
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
import sklearn
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist, jaccard
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def myinfo(request):
    staticss = Statics.objects.all()
    static01s = Statics.objects.filter(kcode=20001)
    static02s = Statics.objects.filter(kcode=20002)
    static03s = Statics.objects.filter(kcode=20003)
    static04s = Statics.objects.filter(kcode=20004)
    static05s = Statics.objects.filter(kcode=20005)
    static06s = Statics.objects.filter(kcode=20006)
    static07s = Statics.objects.filter(kcode=20007)

    persons = Person.objects.filter(id=2018038004)
    person_ob= Kiosk.objects.filter(kioskcode=20001)

    context = {'persons': persons, 'person_ob': person_ob, 'staticss': staticss, 'static01s': static01s, 'static02s': static02s,
               'static03s': static03s, 'static04s': static04s, 'static05s': static05s, 'static06s': static06s, 'static07s': static07s}
    return render(request, 'first/myinfo.html', context)

def charts(request):
    staticss = Statics.objects.all()
    static01s = Statics.objects.filter(kcode=20001)
    static02s = Statics.objects.filter(kcode=20002)
    static03s = Statics.objects.filter(kcode=20003)
    static04s = Statics.objects.filter(kcode=20004)
    static05s = Statics.objects.filter(kcode=20005)
    static06s = Statics.objects.filter(kcode=20006)
    static07s = Statics.objects.filter(kcode=20007)
    static08s = Statics.objects.filter(kcode=20008)
    static09s = Statics.objects.filter(kcode=20009)
    static10s = Statics.objects.filter(kcode=20010)
    static11s = Statics.objects.filter(kcode=20011)
    static12s = Statics.objects.filter(kcode=20012)
    static13s = Statics.objects.filter(kcode=20013)
    static14s = Statics.objects.filter(kcode=20014)
    static15s = Statics.objects.filter(kcode=20015)
    static16s = Statics.objects.filter(kcode=20016)
    static17s = Statics.objects.filter(kcode=20017)
    static18s = Statics.objects.filter(kcode=20018)
    static19s = Statics.objects.filter(kcode=20019)
    static20s = Statics.objects.filter(kcode=20020)
    static21s = Statics.objects.filter(kcode=20021)
    static22s = Statics.objects.filter(kcode=20022)
    static23s = Statics.objects.filter(kcode=20023)
    static24s = Statics.objects.filter(kcode=20024)
    static25s = Statics.objects.filter(kcode=20025)
    static26s = Statics.objects.filter(kcode=20026)
    static27s = Statics.objects.filter(kcode=20027)
    static28s = Statics.objects.filter(kcode=20028)
    static29s = Statics.objects.filter(kcode=20029)
    static30s = Statics.objects.filter(kcode=20030)
    context = {'staticss': staticss, 'static01s': static01s, 'static02s': static02s, 'static03s': static03s,
               'static04s': static04s, 'static05s': static05s, 'static06s': static06s, 'static07s': static07s,
                'static08s': static08s, 'static09s': static09s, 'static10s': static10s,
               'static11s': static11s, 'static12s': static12s, 'static13s': static13s,
               'static14s': static14s, 'static15s': static15s, 'static16s': static16s, 'static17s': static17s,
               'static18s': static18s, 'static19s': static19s, 'static20s': static20s,
               'static21s': static21s, 'static22s': static22s, 'static23s': static23s,
               'static24s': static24s, 'static25s': static25s, 'static26s': static26s, 'static27s': static27s,
               'static28s': static28s, 'static29s': static29s, 'static30s': static30s,
               }
    return render(request, 'first/charts.html', context)


def tables(request):
    kstates = Kstate.objects.all()
    context = {'kstates': kstates}
    return render(request, 'first/tables.html', context)

def login(request):
    try:
        request.session['userid']
        return HttpResponseRedirect(reverse('first/login'))
    except:
        return render(request, 'first/login.html')


def sign_in(request):
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    try:
        user = User.objects.get(userid=user_id, password=user_pw)
        request.session['userid'] = user_id
        return HttpResponseRedirect(reverse('myinfo'))
    except User.DoesNotExist:
        return HttpResponse('실패')


def sign_up(request):
    return render(request, 'first/signup.html')

def join(request):
    user_id = request.POST['id']
    user_pw = request.POST['pw']
    user_name = request.POST['name']
    try:
        user = User.objects.get(userid=user_id)
        return HttpResponse('이미 존재하는 아이디')
    except User.DoesNotExist:
        user = User(userid=user_id, password=user_pw, username=user_name)
        user.save()

        keywords = SubjectKeyword.objects.all()
        for keyword in keywords:
            UserKeyword.objects.update_or_create(
                user_id=user.id,
                keyword_id=keyword.keyword_id,
                keyword=keyword.keyword,
                flag=0
            )
        request.session['userid'] = user_id
        return HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(reverse('first/signup'))



# def myinfo(request):
#     keyword_list = []
#     try:
#         user = User.objects.get(userid=request.session['userid'])
#         user_keyword = []
#         try:
#             keywords = SubjectKeyword.objects.all()
#             try:
#                 user_keyword = get_list_or_404(UserKeyword, user_id=user.id)
#             except:
#                 pass
#             """
#             page = int(request.GET.get('p',1))
#             paginator = Paginator(keywords,5)
#             queryset1 = paginator.get_page(page)
#             try:
#                 contacts = paginator.page(page)
#             except PageNotAnInteger:
#                 contacts = paginator.page(1)
#             except EmptyPage:
#                 contacts = paginator.page(paginator.num_pages)
#             """
#             paginator = Paginator(keywords, 5)
#
#             page_number = request.GET.get('page')
#             page_obj = paginator.get_page(page_number)
#
#             keywords = SubjectKeyword.objects.all()
#             if len(keywords) > len(user_keyword):
#                 for keyword in keywords:
#                     try:
#                         UserKeyword.objects.get(user_id=user.id, keyword_id=keyword.keyword_id)
#                     except:
#                         UserKeyword.objects.update_or_create(
#                             user_id=user.id,
#                             keyword_id=keyword.keyword_id,
#                             keyword=keyword.keyword,
#                             flag=0
#                         )
#                 user_keyword = get_list_or_404(UserKeyword, user_id=user.id)
#         except:
#             pass
#         return render(request, 'first/myinfo.html', {'user': get_object_or_404(User, userid=request.session['userid']),
#                                                     'user_keywords': user_keyword, 'page_obj': page_obj})
#     except KeyError:
#         return HttpResponseRedirect(reverse('index'))

def keyword(request, id):
    try:
        user = User.objects.get(userid=request.session['userid'])
        user_keyword = UserKeyword.objects.get(user_id=user.id, keyword_id=id)
        if user_keyword.flag == 0:
            user_keyword.flag = 1
        else:
            user_keyword.flag = 0
        user_keyword.save()
        return HttpResponseRedirect(reverse('myinfo'))
    except KeyError:
        return HttpResponseRedirect(reverse('myinfo'))


def page_profile(request):
    return render(request, 'first/page-profile.html')
