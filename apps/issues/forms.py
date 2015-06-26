from django import forms


class SourceForm(forms.Form):
    name = forms.CharField(label="Source Name")
    type = forms.ChoiceField(label="Source Type", choices=[("jira", "JIRA"), ("github", "GitHub")])
    url = forms.URLField(label="Source URL")
    required = forms.CharField(label="Required Info", widget=forms.Textarea)
