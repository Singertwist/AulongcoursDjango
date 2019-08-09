from django import forms
from .models import Comments

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('nom', 'email', 'message',)
