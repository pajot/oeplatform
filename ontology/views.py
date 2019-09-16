from django.shortcuts import render
from django.views import View
from .stardog import load_all_classes, load_subject, load_individuals, load_all_scenarios, load_all_properties
# Create your views here.

class Overview(View):
    def get(self, request):
        return render(request,
                      'ontology/overview.html',
                      context={'classes': load_all_classes(),
                               'scenarios': load_all_scenarios()})


class Subject(View):
    def get(self, request, database, iri):
        data = load_subject(iri, database=database)
        individuals = load_individuals(iri)
        return render(request,
                      'ontology/subject.html',
                      context={'title': iri, 'properties': reversed(list(data)), 'individuals': individuals})

class Search(View):
    def get(self, request):
        classes = {x for x,_,_ in load_all_classes()}
        properties = {x for x,_ in load_all_properties()}
        return render(request,
                      'ontology/search.html',
                      context={'classes': classes, 'properties': properties, 'scenarios': reversed(list(load_all_scenarios()))})
