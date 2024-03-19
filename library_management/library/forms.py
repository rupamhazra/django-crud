from django import  forms
from library.models import *


class addbookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=('id','book_name','book_publisher','book_publish_date')