from django.contrib import admin
from django.urls import path

from base.views import SubmitThanksView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('thanks/', SubmitThanksView.as_view(), name='submit_thanks'),
]
