from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls import reverse

from base.forms import PackageRequestForm


class IndexPage(TemplateView):
    template_name = 'pages/index.html'


class SubmitView(FormView):
    form_class = PackageRequestForm
    success_url = reverse('submit_thanks')


class SubmitThanksView(TemplateView):
    template_name = 'pages/thanks.html'
