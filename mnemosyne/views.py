"""
Finds the template file
Renders it into HTML
Wraps it in an HTTP response
Sends it back to the browser
"""

from django.shortcuts import render

def index(request):
    return render(request, 'mnemosyne/index.html')
