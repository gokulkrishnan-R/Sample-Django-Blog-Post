from django import forms
from.models import Profile,Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=("user","image","bio","phone_no","facebook","instagram","linkedin")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('post','name','comment_body','posted_on')
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control"}),
            'comment_body':forms.TextInput(attrs={"class":"form-control"})
        }

"""
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('name','image')
"""