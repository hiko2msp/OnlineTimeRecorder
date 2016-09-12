from django.shortcuts import render
from .forms import MyForm
from .models import SyainData

def form_test(request):
   form = MyForm()
   return render(request, 'polls/form.html', {
       'form': form,
   })
   
def search(request):
   phone_number = dict(request.GET)['query'][0]
   result_list = []
   for row in SyainData.objects.filter(phone=phone_number):
      result_list.append(row)
   return render(request, 'polls/form.html', {
      'message': u'検索結果は{}件です'.format(len(result_list)),
      'form': MyForm(),
      'search_result': result_list
   })
   
def form_save(request):
   form = MyForm(request.POST)
   if form.is_valid():
      ret_dict = dict(request.POST)
      syain = SyainData(
            phone=ret_dict['phone'][0],
            password=ret_dict['password'][0],
            name=ret_dict['name'][0],
            corporation_name=ret_dict['corporation_name'][0],
            date=ret_dict['date'][0],
            job_start=ret_dict['job_start'][0],
            job_end=ret_dict['job_end'][0],
            status=ret_dict['status'][0],
            min=ret_dict['min'][0],
            max=ret_dict['max'][0],
            overtime=ret_dict['overtime'][0]
         )
      syain.save()
      message = u'登録が完了しました'
   else:
      message = u'登録に失敗しました'
      
   return render(request, 'polls/form.html', {
      'message': message,
      'form': MyForm(),
   }) 
   
   
#   <button type='submit' name='action' value='send'>
   