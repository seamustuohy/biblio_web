"""biblio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.urls import path, include
from update_info import views



# Get a URL prefix if it exists
try:
    PREFIX = os.environ["BW_URL_PREFIX"]
    if PREFIX == "":
        PREFIX = None
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e

bw_patterns = [
    path('update_doc_info/', views.UpdateForm, name='update_doc_info')
]

if PREFIX is None:
    urlpatterns = bw_patterns
else:
    if PREFIX.endswith('/') is False:
        PREFIX += "/"
    urlpatterns = [
        path(PREFIX, include(bw_patterns))
    ]
