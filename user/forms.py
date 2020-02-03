
'''
hello
'''
from django import forms

class RegisterFrom(forms.Form):
    '''
    create user form
    '''
    email = forms.EmailField(error_message={'required': '이메일을 입력해주세요!'}, max_length=64, label='이메일')

    password = forms.CharField(error_message={'required': '비밀번호를 입력해주세요!'}, widget=forms.PasswordInput, label='비밀번호')

    re_password = forms.CharField(error_message={'required': '비밀번호를 한번더 입력해주세요!'}, widget=forms.PasswordInput, label='비밀번호 확인')