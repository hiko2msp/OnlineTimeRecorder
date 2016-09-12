from django import forms
class MyForm(forms.Form):
    phone = forms.CharField(max_length=13,default='000-0000-0000')
    name = forms.CharField(max_length=30,default='sei-mei')
    corporation_name = forms.CharField(max_length=30,default='corpration-name')
# expire_date = models.DateField(max_length=10,default='0000-00-00')
    job_start = forms.IntegerField(max_length=5,default=0)
    job_end = forms.IntegerField(max_length=5,default=0)
    status = forms.CharField(max_length=2,default='休暇')
    min = forms.IntegerField(max_length=5,default=14000)
    max = forms.IntegerField(max_length=5,default=18000)
    overtime = forms.IntegerField(max_length=6,default=0)