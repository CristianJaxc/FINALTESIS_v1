from django.forms import *

class Report_Form(Form):
    date_range = CharField(widget=TextInput(attrs={
        'class' : 'form-control',
        'autocomplete' : 'off',
    }))

