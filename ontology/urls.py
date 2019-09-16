from django.conf.urls import url

from ontology import views

urlpatterns = [
    url(r'^$', views.Overview.as_view(), {}),
    url(r'^search$', views.Search.as_view(), {}),
    url(r'^(?P<database>(knowledge|oeo))/(?P<iri>[A-z_0-9]+)$', views.Subject.as_view(), {}),
    url(r'^v(?P<major>[0-9]+).(?P<minor>[0-9]+).(?P<patch>[0-9]+)/(?P<database>(knowledge|oeo))/(?P<iri>[A-z_0-9]+)$', views.Subject.as_view(), {}),


]
