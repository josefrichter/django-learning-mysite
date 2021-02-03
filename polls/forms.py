from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    """ Form for the Question model """
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'image')