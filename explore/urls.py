from django.urls import path
from .views import ExploreListView


urlpatterns = [

    path("", ExploreListView.as_view(), name="explore-list"),

]