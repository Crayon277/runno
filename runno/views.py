from django.template import Template, Context

from django.http import HttpResponse

import datetime

def current_time(request):
    now = datetime.datetime.now()
    templates = Templates("<html><body>It is now {{crrent_date}}</body></html>")
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def about (request):
    return HttpResponse("Hello World!")


