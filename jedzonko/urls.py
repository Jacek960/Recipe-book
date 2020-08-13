from django.urls import path

from jedzonko.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),

]