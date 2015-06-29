from django import forms
from .models import IssueSource

class SourceForm(forms.Form):
    name = forms.CharField(label="Source Name")
    type = forms.ChoiceField(label="Source Type", choices=[("jira", "JIRA"), ("github", "GitHub")])
    url = forms.URLField(label="Source URL")
    required = forms.CharField(label="Required Info", widget=forms.Textarea)

    def __init__(self, dict=None, source=None):
        if source:
            super(SourceForm, self).__init__({
                "name": source.name,
                "url": source.base_url,
                "type": source.source_type,
                "required": source.required_info
            })
        else:
            super(SourceForm, self).__init__(dict)


    def build_source(self):

        source = IssueSource()
        return self.set_source(source)

    def set_source(self, source):
        if not self.is_valid():
            return None
        values = self.cleaned_data
        source.name = values["name"]
        source.base_url = values["url"]
        source.source_type = values["type"]
        source.required_info = values["required"]
        return source