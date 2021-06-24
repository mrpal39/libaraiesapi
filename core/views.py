
import json
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render, HttpResponse
import requests
from requests.api import get
from .api import api_endpoint, url_lib
import os
from django.http import JsonResponse
from urllib.parse import urlencode,unquote_plus,unquote
from django.views import View
from django.utils.http import urlencode ,urlunquote_plus,urlquote


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
    name = unquote(nam)
    print(name)  
    
    
    d_platform = f"/api/{platform}/{name}"
    print(d_platform)
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
    name = ""

    if request.method == 'GET':

        owner = request.GET.get('q')
        name = request.GET.get('q')
    Repoown = f"/api/github/{owner}"

    # Repository = f"/api/github/{owner}/repositories"
    # projects = f"/api/github/{owner}/projects"
    # # project_CON = f"/api/github/{owner}/project-contributions"
    # dependencies = f"/api/github/{owner}/dependencies"
    # repository = f"/api/github/{owner}/repository-contributions"
    # Repositor = "/api/github/mrpal39/subscriptions"

    dependents = f"/api/github/{owner}/{name}/"
    path = f"/api/github/{owner}/{name}/dependencies"
    pathprojects = f"/api/github/{owner}/{name}/projects"
    dependent_repositories = f"/api/github/{owner}/{name}/dependent_repositories"
    contributors = f"/api/github/{owner}/{name}/contributors"
    contributors = f"/api/github/{owner}/{name}/sourcerank"
    # print(owner)

    # own= api_endpoint.url(Repoown)
    # a = api_endpoint.url(Repository)
    # project = api_endpoint.url(projects)
    # project_c = api_endpoint.url(Repositor)
    # project_d= api_endpoint.url(dependents)
    content = {
        # 'Repository': a,
        # 'project_d': project_d,
        # 'project': project,
        # 'proj':project_c,
        # 'user':own,

    }
    return render(request, "github.html", content)


def github_user_login(request):
    owner = ""
    name = ""

    if request.method == 'GET':

        owner = request.GET.get('q')
        # name = request.GET.get('q')

    # Repository =
    # projects =
    # # project_CON =
    # dependencies = f"/api/github/{owner}/dependencies"
    # repository = f"/api/github/{owner}/repository-contributions"
    # Repositor =

    own = api_endpoint.url(f"/api/github/{owner}")
    Repository = api_endpoint.url(f"/api/github/{owner}/repositories")
    project = api_endpoint.url(f"/api/github/{owner}/projects")
    contributions = api_endpoint.url(
        f"/api/github/{owner}/project-contributions")
    # project_d= api_endpoint.url(repository)
    content = {
        'Repository': Repository,
        # 'project_d': project,
        'project': project,
        'contributions': contributions,
        'user': own,

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
# def api_search(request):

    # qa = ""
    # sort = ""
    # if request.method =="GET":           
    #     qa = request.GET.get('qa')
    #     sort = request.GET.get('sort')
        
 
    # print(qa)  
    # print(sort)
    # path = '/api/search'
    # payload = {
    #     'platform': qa,
    #     'sort': sort,
    #     'api_key': api_key,
    # }
    # query = urlencode(payload)
    # dat = api_endpoint.base_url(path, query)
    # # print(dat)
    # response = {
    #     'qa': qa,
    #     'conme': dat,
    # }
    # # return JsonResponse(response)
    # return render(request, 'search.html', response)


def api_search_data(request):
    qa = {}
    sort = ""
    qa = request.GET.get('q')
    sort = request.GET.get('sort')
 
    path = '/api/search'
    payload = {
        'q': qa,
        'sort': sort,
        
        'api_key': api_key,
    }
    query = urlencode(payload)
    dat = api_endpoint.base_url(path, query)
    # print(dat)
    response = {
        'qa': qa,
        'conme': dat,
    }
  
    return render(request, 'search.html', response)
