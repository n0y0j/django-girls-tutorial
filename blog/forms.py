from django import forms
from .models import Post

# 만들 폼의 이름
class PostForm(forms.ModelForm):
    #폼을 만들기 위해 어떤 모델이 쓰이는지 가르쳐줌
    class Meta:
        model = Post
        fields = ('title', 'text',)