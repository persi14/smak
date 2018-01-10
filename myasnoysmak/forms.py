from django import forms
from django.utils.translation import ugettext_lazy as _

class Add_Review(forms.Form):

	author = forms.CharField(label=_('Ваше имя(ФИО):'), required=True, widget=forms.TextInput(attrs={'style':'width:90%; height:30px; color:black'}), max_length=150)
	text = forms.CharField(label=_('Ваш отзыв :'), required=True, widget=forms.Textarea(attrs={'style':'width:90%; min-height:100px; color:black'}),)


