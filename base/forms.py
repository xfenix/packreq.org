from django.forms import ModelForm


class PackageRequestForm(ModelForm):
    class Meta:
        model = PackageRequest
