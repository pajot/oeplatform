from rdflib.plugins.stores import sparqlstore
from rdflib import Graph
from oeplatform.securitysettings import RDF_DATABASES, URL
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

from django.forms import Widget

OEO_ENDPOINT = 'http://{host}:{port}/{name}/query'.format(**RDF_DATABASES['oeo'])
KNOWLEDGE_ENDPOINT = 'http://{host}:{port}/{name}/query'.format(**RDF_DATABASES['knowledge'])

_ONTOLOGY_URL = 'http://openenergy-platform.org/ontology/'
_OEO_URL = _ONTOLOGY_URL + 'oeo/'
_KNOWLEDGE_URL = _ONTOLOGY_URL + 'knowledge/'

_ONTOLOGY_URL_V = 'http://openenergy-platform.org/ontology/v0.0.1/'
_OEO_URL_V = _ONTOLOGY_URL_V + 'oeo/'
_KNOWLEDGE_URL_V = _ONTOLOGY_URL_V + 'knowledge/'


# TODO: This should be dynamic!

_PREFIX = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema',
    'owl': 'http://www.w3.org/2002/07/owl',
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'dc': 'http://purl.org/dc/elements/1.1',
    'foaf': 'http://xmlns.com/foaf/0.1',
    'oek': _ONTOLOGY_URL + 'knowledge',
    'oeo': _ONTOLOGY_URL + 'oeo',
}
_INV_PREFIX = {v:k for k,v in _PREFIX.items()}


def localise(string):
    if not isinstance(string, str):
        return string
    else:
        return string.replace('openenergy-platform.org', URL)


def use_prefix(string):
    if '#' in string:
        prefix, name = string.split('#')
    else:
        parts = string.split('/')
        prefix = '/'.join(parts[:-1])
        name = parts[-1]
    if prefix in _INV_PREFIX:
        return (_INV_PREFIX[prefix] + ':' + name, localise(string))
    else:
        return (string, localise(string))


def load_all_scenarios():
    query = 'select ?s ?l ?d where { ' \
            '?s a oeo:Scenario . ' \
            'optional {?s <http://purl.obolibrary.org/obo/IAO_0000115> ?d}' \
            'optional {?s rdfs:label ?l}' \
            '}'
    for subject, label, type in request(query, KNOWLEDGE_ENDPOINT):
        if label:
            ref = localise(subject)
        else:
            label, ref = use_prefix(subject)
        yield label, ref, type


def load_all_classes():
    query = 'select ?s ?d where { ' \
            '?s a <http://www.w3.org/2002/07/owl#Class>. ' \
            'optional {?s <http://purl.obolibrary.org/obo/IAO_0000115> ?d}' \
            'filter (regex(str(?s), "^'+_OEO_URL+'.+"))' \
            '}'
    for subject, definition in request(query, OEO_ENDPOINT):
        label, ref = use_prefix(subject)
        yield label, ref, definition

def load_individuals(cls_iri):
    query = 'select ?s (sample(?d) as ?description) where {{ ' \
            '?s a <http://www.w3.org/2002/07/owl#NamedIndividual>,' \
            '     <{iri}>.' \
            'optional {{?s <http://purl.obolibrary.org/obo/IAO_0000115> ?d}}' \
            '}}' \
            'group by ?s'.format(iri=_OEO_URL+cls_iri)

    for subject, definition in request(query, OEO_ENDPOINT):
        label, ref = use_prefix(subject)
        yield label, ref, definition

    query = 'select ?s (sample(?d) as ?description) where {{ ' \
            '?s a <{iri}>.' \
            'optional {{?s <http://purl.obolibrary.org/obo/IAO_0000115> ?d}}' \
            '}}' \
            'group by ?s'.format(iri=_OEO_URL + cls_iri)

    for subject, definition in request(query, KNOWLEDGE_ENDPOINT):
        label, ref = use_prefix(subject)
        yield label, ref, definition

def load_subject(iri, database='oeo'):
    endpoint = None
    if database == 'knowledge':
        iri = _KNOWLEDGE_URL + iri
        endpoint = KNOWLEDGE_ENDPOINT
    elif database == 'oeo':
        iri = _OEO_URL + iri
        endpoint = OEO_ENDPOINT

    query = 'select ?p (group_concat (distinct ?o ; separator = ";") as ?items) ' \
            'where {{ <{iri}> ?p ?o }} group by ?p'.format(iri=iri)
    for predicate, objects in request(query, endpoint):
        if predicate is not None:
            name, ref = use_prefix(predicate)
            yield name, ref, [use_prefix(o) for o in objects.split(';')]


def request(query, endpoint):
    """
    :param query: A SPARQL-Query
    :param endpoint: A RDFLib connection string
    :return:
    """
    store = sparqlstore.SPARQLStore()
    store.open(endpoint)
    return store.query(query)
