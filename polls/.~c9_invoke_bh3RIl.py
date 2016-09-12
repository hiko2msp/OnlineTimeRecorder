from django.shortcuts import render
from .forms import MyForm


def form_test(request):
   form = MyForm()
   return render(request, 'polls/form.html', {
       'form': form,
   })
def form_save(request):
def save(request):
   form = MyForm()
   return render(request, 'templates/polls/form.html', {
       'form': form,
   })   
#   <button type='submit' name='action' value='send'>
   