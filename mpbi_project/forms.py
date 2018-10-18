from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        # help_text='Write here your message!'
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)

    #def clean(self):
        #cleaned_data = super(ContactForm, self).clean()
       # name = cleaned_data.get('name')
       # email = cleaned_data.get('email')
        #message = cleaned_data.get('message')
        # if not name and not email and not message:
        #raise forms.ValidationError('Заполните пожалуйста форму чтобы связаться с нами!')
