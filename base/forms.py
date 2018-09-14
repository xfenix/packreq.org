from django.forms import ModelForm

from base.models import PackageRequest


class PackageRequestForm(ModelForm):
    class Meta:
        model = PackageRequest
        fields = '__all__'
