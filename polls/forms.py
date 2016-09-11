from django import forms
import datetime
time_difference = datetime.timedelta(hours=9)

class MyForm(forms.Form):
    current_time = datetime.datetime.now() + time_difference
    
    phone = forms.CharField(label=u'電話番号')
    password = forms.CharField(label=u'パスワード')
    name = forms.CharField(label=u'氏名')
    corporation_name = forms.CharField(label=u'会社名')
    date = forms.DateField(
        label=u'日付',
        input_formats=['%Y-%m-%d'],
        initial=datetime.date.today())
    job_start = forms.TimeField(
        label=u'出勤時間',
        input_formats=['%H:%M'],
        initial=current_time.strftime('%H:%M'))
    job_end = forms.TimeField(
        label=u'退社時間',
        input_formats=['%H:%M'],
        initial=current_time.strftime('%H:%M'))
    status = forms.CharField(label=u'状態')
    min = forms.TimeField(
        label=u'最小時間',
        input_formats=['%H:%M']
        )
    max = forms.TimeField(
        label=u'最大時間',
        input_formats=['%H:%M']
        )
    overtime = forms.TimeField(
        label=u'残業時間',
        input_formats=['%H:%M'],
        )