# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from django.urls import reverse

from django.views import generic

from .models import Question, Choice

import os

import json

global list

list = { 
        'A':{'file_list':[{'name':'A1', 'contri':0.1234567}, {'name':'A2', 'contri':0.987654}]}, 
        'A1':{'file_list':[{'name':'B1', 'contri':0.1234567}, {'name':'B2', 'contri':0.987654}]}, 
        'A2':{'file_list':[{'name':'C1', 'contri':0.1234567}, {'name':'C2', 'contri':0.987654}]}, 
        }



global meta_dict

json_file='./meta.json'
meta_dict = {}

with open(json_file) as fd1:
    message = json.load(fd1)


## fot github test
for item in message:
    meta_dict[item] = message[item]

print meta_dict

for item in meta_dict:
    print item
    print ':::::::::::::'
    for file_info in meta_dict[item]['file_list']:
        print file_info
    print '\n'

def default_page(request):
    return HttpResponse("Welcome, default page of APP polls")

class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except  (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

class JsonListView(generic.ListView):
    context_object_name = 'children_list'
    template_name = 'polls/jsonlist.html'

    def get_queryset(self):
        json_file = "/home/wangpengfei.pfwang/devroot/000/workdir/django/ByGithub/FirstDjangoPrj/mysite/meta.json"
        with open(json_file) as fd:
                message = json.load(fd)

        children_list = []

        for obj in message['object']:
            if message['object'][obj]['children']:
                for inc in message['object'][obj]['children']:
                    one = {'contri': inc['contribution'], 'name': inc['name']}
                    children_list.append(one)

        #children_list = ['a_file', 'b_file', 'c_file']
        return children_list

def root_list(request):
    file_list = meta_dict['root']
    return render(request, 'polls/list.html', file_list)

def node_list(request, node_name):
    file_list = meta_dict[node_name]
    return render(request, 'polls/list.html', file_list)





