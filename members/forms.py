from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from thesite.models import Profile, Category,Occupation


choices = Occupation.objects.all().values_list('occupation_name','occupation_name')
choice_list1 = []
 
for item in choices:
  choice_list1.append(item)

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
 
for item in choices:
    choice_list.append(item)


print(choice_list)
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url', 'linkedin_url', 'interest', 'interest2', 'interest3','occupation')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write about yourself'}),
            #'profile_pic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title your idea here'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link to your personal website'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link to your Facebook profile'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link to your Twitter profile'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link to your Instagram profile'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link to your Pinterest profile'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link to your Linkedin profile'}),
            'interest': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': 'What topics are you interested in?'}),
            'interest2': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': 'What topics are you interested in?'}),
            'interest3': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': 'What topics are you interested in?'}),
            'occupation': forms.Select(choices = choice_list1, attrs={'class': 'form-control', 'placeholder': 'What is your current occupation?'}),
           
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
         

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


