from abc import ABC
from django.utils.html import format_html, format_html_join, mark_safe
from itertools import chain
from rdflib import Graph

from modelview.rdf import handler, field
from modelview.rdf.namespace import *


class RDFFactory(handler.Rederable, ABC):
    _field_handler = {}
    _direct_parent = None
    classes = field.Field(rdf_name=rdf.type, verbose_name="Classes")
    _label_iri = rdfs.label

    @classmethod
    def doc(self):
        s = f"""Factory class for {self._direct_parent}. This class has the following fields: 

"""
        for f in self.iter_field_names():
            field = getattr(self,f)
            s += f"* `{f} <{field.rdf_name}>`_"
            if field.help_text is not None:
                s+= ": " + field.help_text
            s += "\n"
        s += "\n"
        return s

    def __init_subclass__(cls, **kwargs):
        cls._field_handler = {k.rdf_name: k.handler for k in cls.iter_fields()}
        cls._field_map = {getattr(cls, k).rdf_name: k for k in cls.iter_field_names()}
        cls.__doc__ = cls.doc()

    def __init__(self, **kwargs):
        self.additional_fields = {}
        default_handler = handler.DefaultHandler()
        _internal_fields = set(self.iter_field_names())
        for k0, v in kwargs.items():
            k = self._field_map.get(k0, k0)
            if k in _internal_fields:
                getattr(self, k).values = v
            else:
                self.additional_fields[k] = v

    @classmethod
    def iter_fields(cls):
        """Returns an iterator of all fields in this factory"""
        return (getattr(cls, k) for k in cls.iter_field_names())

    @classmethod
    def iter_field_names(cls):
        """Returns an iterator of all field names in this factory"""
        for k in dir(cls):
            if isinstance(getattr(cls, k, None), field.Field):
                yield k

    @classmethod
    def _load_many(cls, identifiers, context, graph: Graph):
        graph += context.describe(identifiers)
        d = {i: cls._parse(i, context, graph) for i in identifiers}
        return d

    @classmethod
    def _load_one(cls, identifier, context, graph: Graph):
        graph += context.describe([identifier])
        return cls._parse(identifier, context, graph)

    @classmethod
    def _parse(cls, identifier, context, graph: Graph, cache=None):
        if cache is None:
            cache = dict()
        obj = cache.get(identifier, dict())
        for p, o in graph.predicate_objects(identifier):
            try:
                obj[p].append(o)
            except KeyError:
                obj[p] = [o]
        res = cache[identifier] = cls(**{p: cls._field_handler.get(p, handler.DefaultHandler())(os, context, graph) for p, os in obj.items()})
        return res

    def save(self, context):
        triples = chain(*(k.to_triples(self.iri) for k in self.iter_fields()), (f"{self.iri} {k} {v}" for k, vs in self.additional_fields.items() for v in vs))
        print("\n".join(triples))

    def render(self, **kwargs):
        return format_html(mark_safe("<table class=\"table\">{}</table>"), self.render_table())

    def render_table(self):
        s = format_html_join("\n", "{}", ((f.render(),) for f in self.iter_fields()))
        return s

    @property
    def label(self):
        return getattr(self, self._label_iri)


class Scenario(RDFFactory):
    abbreviation = field.Field(rdf_name=dbo.abbreviation, verbose_name="Abbreviation")
    abstract = field.Field(rdf_name=dbo.abstract, verbose_name="Abstract", help_text="A short description of this scenario")
    name = field.Field(rdf_name=foaf.name, verbose_name="Abstract", help_text="A short description of this scenario")


class AnalysisScope(RDFFactory):
    is_defined_by = field.Field(rdf_name=OEO.OEO_00000504, verbose_name="is defined by")
    covers_sector = field.Field(rdf_name=OEO.OEO_00000505, verbose_name="Sectors")
    covers = field.Field(rdf_name=OEO.OEO_00000522, verbose_name="Covers")


class Publication(RDFFactory):
    title = field.Field(rdf_name=dc.title, verbose_name="Title", help_text="Title of the publication")
    subtitle = field.Field(rdf_name=dbo.subtitle, verbose_name="Subtitle")
    publication_year = field.Field(rdf_name=npg.publicationYear, verbose_name="Publication year", help_text="Year this publication was published in")
    abstract = field.Field(rdf_name=dbo.abstract, verbose_name="Abstract", help_text="Abstract of the publication")
    url = field.Field(rdf_name=schema.url, verbose_name="URL", help_text="Link to this publication")
    authors = field.Field(rdf_name=OEO.OEO_00000506, verbose_name="Authors", help_text="Authors of this publication")
    about = field.Field(rdf_name=obo.IAO_0000136, verbose_name="About", help_text="Elements of this publication")


class Institution(RDFFactory):
    _direct_parent = OEO.OEO_00000238
    name = field.Field(rdf_name=foaf.name, verbose_name="Name")


class Study(RDFFactory):
    _direct_parent = OEO.OEO_00020011
    funding_source = field.Field(rdf_name=OEO.OEO_00000509, verbose_name="Funding source", handler=handler.FactoryHandler(Institution))
    has_part = field.Field(rdf_name=obo.BFO_0000051, verbose_name="Has part")
    covers_energy_carrier = field.Field(rdf_name=OEO.OEO_00000523, verbose_name="Covers energy carriers")
    model_calculations = field.Field(rdf_name=schema.affiliation, verbose_name="Model Calculations")


class Person(RDFFactory):
    _direct_parent = OEO.OEO_00000323
    first_name = field.Field(rdf_name=foaf.givenName, verbose_name="First name")
    last_name = field.Field(rdf_name=foaf.familyName, verbose_name="Last name")
    affiliation = field.Field(rdf_name=schema.affiliation, verbose_name="Affiliation")


class Model(RDFFactory):
    _direct_parent = OEO.OEO_00020011
    url = field.Field(rdf_name=schema.url, verbose_name="URL")
    name = field.Field(rdf_name=dc.title, verbose_name="Name")


class ModelCalculation(RDFFactory):
    has_input = field.Field(rdf_name=obo.RO_0002233, verbose_name="Inputs")
    has_output = field.Field(rdf_name=obo.RO_0002234, verbose_name="Outputs")
    uses = field.Field(rdf_name=OEO.OEO_00000501, verbose_name="Involved Models", handler=handler.FactoryHandler(Model))
