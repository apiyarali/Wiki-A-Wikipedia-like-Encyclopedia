from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(
        attrs={
            'class':'form-control'
            }
    ))
    content = forms.CharField(label="Content", widget=forms.Textarea(
        attrs={
            'class':'form-control'
            }
    ))

class EditPageForm(forms.Form):
    content = forms.CharField(label="Content", widget=forms.Textarea(
        attrs={
            'class':'form-control'
            }
    ))