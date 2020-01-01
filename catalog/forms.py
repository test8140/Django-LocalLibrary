from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy
import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField()

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
    
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - reneval in past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - reneval in more than 4 weeks ahead'))
        return data
     