from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from class_app import models
from django.urls import reverse_lazy
# Create your views here.

class indexView(TemplateView):
    template_name='class_app/index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['text1']='I am text1'
        context['text2']='I am text2'
        return context

class indexListView(ListView):
    context_object_name='musician_list'
    model=models.Musician
    template_name='class_app/indexList.html'


class musicianDetails(DetailView):
    context_object_name='musician_list'
    model=models.Musician
    template_name='class_app/musicianDetail.html'


class addMusician(CreateView):
    fields=('first_name','last_name','instrument')
    model=models.Musician
    template_name='class_app/musicianAdd.html'


class updateMusician(UpdateView):
    fields=('first_name','instrument')
    model=models.Musician
    template_name='class_app/musicianAdd.html'



class deleteMusician(DeleteView):
    context_object_name='musician_list'
    success_url=reverse_lazy('class_app:indexList')
    model=models.Musician
    template_name='class_app/musicianDelete.html'
