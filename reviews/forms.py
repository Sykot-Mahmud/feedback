from dataclasses import field
from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label="Your Name",required=True,error_messages={'required': 'Please enter your name'})
#     review_text=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(min_value=1,max_value=10)


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        #exlude,list the selected field
        labels={
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating"

        }

        error_messages={
            "user_name":{
                'required': 'Please enter your name',
                'max_length':'please enter a short name'
            },
            
        }
