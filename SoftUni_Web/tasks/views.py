from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from SoftUni_Web.tasks.models import Task


def home(request):
    items = Task.objects.all()
    item_strings = [f'<li>{t.title} - {t.text}</li>' for t in items]
    items_string = ''.join(item_strings)
    html = f"""
    <h1>Vesso is playing with Django</h1>
    <ul>
    {items_string}
    </ul>
    <h1>Vesso is playing with Django again</h1>
    <ol>
    <li>one</li>
    <li>two</li>
    <li>three</li>
    </ol>
    """
    return HttpResponse(html)


def user(request):
    items = Task.objects.all()
    item_strings = [f'<li>{t.title} - {t.text}</li>' for t in items]
    items_string = ''.join(item_strings)
    html = f"""
    <h1>User info</h1>
    <ul>
    {items_string}
    </ul>
    <h1>More user info</h1>
    <ol>
    <li>one</li>
    <li>two</li>
    <li>three</li>
    </ol>
    """
    return HttpResponse(html)

