'''
hi this is user view
'''
from django.shortcuts import render

# Create your views here.


def index(request):
    ''' view function of index.html '''
    return render(request, 'index.html')
