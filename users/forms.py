from unittest.util import _MAX_LENGTH
from django import forms
from . import models
from django.contrib.auth.password_validation import validate_password


class LoginForm(forms.Form):
    personal_id = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': '예) hans', 'autocomplete': 'off'}))
    
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={'placeholder': '비밀번호'}))

    def clean(self):
        personal_id = self.cleaned_data.get('personal_id')
        password = self.cleaned_data.get('password')
        try:
            user = models.User.objects.get(personal_id=personal_id)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    'password', forms.ValidationError('비밀번호가 틀립니다.'))
        except models.User.DoesNotExist:
            self.add_error('personal_id', '존재하지 않는 아이디입니다.')


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('nickname', 'phone_number', 'personal_id', 'username', )
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'placeholder': '비밀번호'}))
    password1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'placeholder': '한번 더 입력해주세요'}))

    def clean_personal_id(self):
        personal_id = self.cleaned_data.get('personal_id')
        try:
            models.User.objects.get(personal_id=personal_id)
            raise forms.ValidationError('이미 가입된 아이디입니다.')
        except models.User.DoesNotExist:
            return personal_id
    def clean_password1(self):
        password=self.cleaned_data.get('password')
        password1=self.cleaned_data.get('password1')
        
        validate_password(password)
        if password != password1:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        else:
            return password
    
    def clean_phone_number(self):
        phone_number=self.cleaned_data.get('phone_number')
        try:
            models.User.objects.get(phone_number=phone_number)
            raise forms.ValidationError('이미 가입된 전화번호입니다.')
        except models.User.DoesNotExist:
            return phone_number
        
    def clean_nickname(self):
        nickname=self.cleaned_data.get('nickname')
        try:
            models.User.objects.get(nickname__iexact=nickname)
            raise forms.ValidationError('존재하는 닉네임입니다.')
        except models.User.DoesNotExist:
            return nickname
        
    def save(self, *args, **kwargs):
        user=super().save(commit=False)
        user.username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user.set_password(password)
        user.nickname=self.cleaned_data.get('nickname')
        user.personal_id=self.cleaned_data.get('personal_id')
        user.save()