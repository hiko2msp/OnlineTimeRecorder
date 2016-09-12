from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Syain # モデルをインポート

def get_fake_employee_database():
    employee_and_status_list = [
        {'name':u'Aさん', 'status':u'出勤'},    
        {'name':u'Bさん', 'status':u'未出勤'},    
        {'name':u'Cさん', 'status':u'退勤後'},    
        {'name':u'Dさん', 'status':u'早退'},    
        {'name':u'Eさん', 'status':u'出張'},    
        {'name':u'Fさん', 'status':u'有給'},   
        {'name':u'Gさん', 'status':u'未出勤'},
    ]
    return employee_and_status_list

def index(request):
    test_variable = 'テストのテキストです'
    test_vartest = '可変値のテストです'
    return render(request,
        'test.html',
        {
            'employee_db': get_fake_employee_database(),
            'test_variable': test_vartest
        }
        )
    
def hello2(request):
    return render(request, 'hello2.html', {})
    
def hello3(request):
    with open('templates/hello3.html') as f:
        html = f.read()
    return HttpResponse(html)
    
def syain_input(request):
    return render(request, 'syain_input.html', {})

def save_syain(request):
    from .models import Syain
    syain_name = request.POST['name']
    syain_status = request.POST['status']
    syain_date = request.POST['date']
    print(syain_name)
    print(syain_status)
    print(syain_date)
    syain = Syain(name=syain_name, status=syain_status, expire_date=syain_date)
    syain.save()
    message = '''
    {0}さんの情報を保存できました。
    状態は、{1}
    有効期限は{2}です。
    '''.format(
        syain_name,
        syain_status,
        syain_date
        )
    return HttpResponse(message)
