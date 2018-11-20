from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from core.utils import AjaxableResponseMixin
from base.forms import PackageRequestForm
from base.models import Language


class IndexPage(TemplateView):
    template_name = 'pages/index.html'


class SubmitView(AjaxableResponseMixin, CreateView):
    form_class = PackageRequestForm
    success_url = reverse_lazy('submit_thanks')


class SubmitThanksView(TemplateView):
    template_name = 'pages/thanks.html'


class LanguageView(ListView):
    template_name = 'pages/language.html'
    model = Language
