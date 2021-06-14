
from django.utils.decorators import method_decorator
from urllib.parse import unquote

from django.shortcuts import redirect, render, HttpResponse
import requests
from requests.api import get
from .api import api_endpoint, url_lib
import os
from django.http import JsonResponse
from urllib.parse import urlencode, unquote_plus
from django.views import View
from django.utils.translation import gettext
from django.utils.http import urlquote


from django.views.decorators.clickjacking import (
    xframe_options_exempt, xframe_options_sameorigin, xframe_options_deny
)

xframe_options_exempt_m = method_decorator(
    xframe_options_exempt, name='dispatch')


api_key = os.getenv("api_key")

# platform="npm"
# name="react"

# class ShowTimeView(TemplateView):  # extend from TemplateView
# template_name = 'github.html'  # add a template_name attribute


def detail_view(request):
    nam = ""
    platform = ""

    if request.method == 'GET':
        platform = request.GET.get('platform')
        nam = request.GET.get('name')

    # print_platform=unquote(platform)
    name = urlquote(nam, safe="")
    d_platform = f"/api/{platform}/{name}"
    # d_version = f"/api/{platform}/{name}/{version}",
    d_dependents = f"/api/{platform}/{name}/dependents"
    # # d_repo = f"/api/{platform}/{name}/dependent_repositories"
    d_cont = f"/api/{platform}/{name}/contributors"
    d_rank = f"/api/{platform}/{name}/sourcerank"

    # a ="/api/Pypi/Django"

    a_con = api_endpoint.url(d_platform)
    # a_version = api_endpoint.url(d_version)
    a_dependents = api_endpoint.url(d_dependents)
    # a_repo = api_endpoint.url(d_repo)
    a_contributors = api_endpoint.url(d_cont)
    a_rank = api_endpoint.url(d_rank)
    # a=repo()

    data = {
        'd': a_con,
        # # 'version': a_version,
        'dependents': a_dependents,
        # # 'repo': a_repo,
        'cont': a_contributors,
        'rank': a_rank,
    }
    # return HttpResponse(data)
    return render(request, "detail_view.html", data)
    # return render(request, self.template_name, content)


def get_github_data(request):
    owner = ""
    # name = ""

    if request.method == 'GET':

        owner = request.GET.get('idgit')
    # name = request.GET.get('name')

    Repository = f"/api/github/{owner}"
    # dependents = f"/api/github/{owner}/{name}/dependents"
    # path = f"/api/github/{owner}/{name}/dependencies"
    # pathprojects = f"/api/github/{owner}/{name}/projects"
    # dependent_repositories = f"/api/github/{owner}/{name}/dependent_repositories"
    # contributors = f"/api/github/{owner}/{name}/contributors"
    # contributors = f"/api/github/{owner}/{name}/sourcerank"
    print(owner)
    a = api_endpoint.url(Repository)
    # a_pathprojects = api_endpoint.url(Repository)

    content = {
        'dependents': a,
        # 'Repository': a_pathprojects
        # 'project': Repository,

    }
    return render(request, "github.html", content)


def home(request):

    return render(request, 'base.html')


def blog(request):
    data = url_lib()
    context = {'data': data}
    if request.method == 'GET':

        # sort = request.GET.get('sort')
        qa = request.GET.get('q')
        print(qa)
    return JsonResponse("okay")

    # return render(request, 'blogs.html', context)


def index(request):

    path = '/api/platforms'
    payload = {
        'api_key': api_key,
    }
    query = urlencode(payload)
    con = api_endpoint.base_url(path, query)
    content = {
        'con': con}
    return render(request, 'index.html', content)


# search baar and search url

@xframe_options_sameorigin
def api_search(request):
    qa = ""

    sort = ""
    if request.method == 'GET':
        # if response.get('X-Frame-Options') is not None:

        sort = request.GET.get('sort')
        qa = request.GET.get('q')

    # else:
    #     qa = "npm"
    # print(qa)
    # print(sort)

    path = '/api/search'
    payload = {
        'q': qa,
        'sort': sort,
        'api_key': api_key,
    }
    query = urlencode(payload)
    dat = api_endpoint.base_url(path, query)
    response = {
        'conme': dat,
    }
    # print ('da')

    return render(request, 'search.html', response)
