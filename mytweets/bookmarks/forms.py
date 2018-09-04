class SearchForm(forms.Form):
    query = forms.CharField( label=u'Enter a keyword to search for', widget=forms.TextInput(attrs={'size': 32}))
