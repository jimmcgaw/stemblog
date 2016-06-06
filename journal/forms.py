from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ basically make all fieldnames bootstrappy """
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field_name, value in self.fields.iteritems():
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Article
        fields = ['title', 'content', 'published_at', 'is_published']
