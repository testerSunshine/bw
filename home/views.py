# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# Create your views here.
from django.template import loader


def index(request):
    context = {}
    template = loader.get_template("app/index.html")
    return HttpResponse(template.render(context, request))


def bw_html(request):
    context = {}
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))