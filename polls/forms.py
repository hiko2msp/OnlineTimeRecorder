from django import forms
import datetime
time_difference = datetime.timedelta(hours=9)

class NameField(forms.CharField):
    def is_zenkaku(self, input_data):
        if input_data != '石塚':
            return False
            
        return True

    @staticmethod 
    def parse_input(input_data):
        return input_data.strip()

    def clean(self, input_data):
        if self.is_zenkaku(input_data):
            cleaned_data = NameField.parse_input(input_data)
            return cleaned_data
        else:
             raise forms.ValidationError('名前が石塚ではありません')
   
class MyForm(forms.Form):
    current_time = datetime.datetime.now() + time_difference
    
    phone = forms.CharField(label=u'電話番号')
    date = forms.DateField(
        label=u'日付',
        input_formats=['%Y-%m-%d'],
        initial=datetime.date.today())
    password = forms.CharField(label=u'パスワード')
    name = NameField(label=u'氏名')
    job_start = forms.TimeField(
        label=u'出勤時間',
        input_formats=['%H:%M'],
        initial=current_time.strftime('%H:%M'))
    job_end = forms.TimeField(
        label=u'退社時間',
        input_formats=['%H:%M'],
        initial=current_time.strftime('%H:%M'))
    status = forms.CharField(label=u'状態')
  