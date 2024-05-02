from rdflib import RDF, Literal

from factsheet.oekg import namespaces
from factsheet.oekg.connection import oekg


class OekgQuery:
    def __init__(self):
        self.oekg = oekg

    def get_related_scenarios_where_table_is_input_dataset(self, table_iri):
        """
        Query the OEKG to get all scenarios that list the current table as
        input dataset.

        Special OEO classes & and relations:
            OEO_00020227 = Scenario Bundle
            OEO_00000365 = Scenario factsheet type (IS STILL IN USE ???)
            RO_0002233 = has_input relation in the oekg

        Args:
            table_iri(str): IRI of any table in the scenario topic on the OEP.
                            IRI Like 'dataedit/view/scenario/abbb_emob'
        """
        related_scenarios = set()

        # Find all scenario bundles
        for s, p, o in self.oekg.triples((None, RDF.type, namespaces.OEO.OEO_00010252)):
            # find all scenarios in any bundle
            for s1, p1, o1 in oekg.triples((s, namespaces.OEKG["has_scenario"], None)):
                # # Find scenarios where the given table is the input dataset
                for s2, p2, o1_input_ds_uid in self.oekg.triples(
                    (o1, namespaces.OEO.RO_0002233, None)
                ):
                    if o1_input_ds_uid is not None:
                        for s3, p3, o3_input_ds_iri in oekg.triples(
                            (
                                o1_input_ds_uid,
                                namespaces.OEO["has_iri"],
                                Literal(table_iri),
                            )
                        ):
                            related_scenarios.add(s2)

        return related_scenarios

    def get_related_scenarios_where_table_is_output_dataset(self, table_iri):
        """
        Query the OEKG to get all scenarios that list the current table as
        output dataset.

        Special OEO classes & and relations:
            OEO_00000365 = Scenario factsheet type
            RO_0002234 = has_output relation in the oekg

        Args:
            table_iri(str): IRI of any table in the scenario topic on the OEP.
                            IRI Like 'dataedit/view/scenario/abbb_emob'
        """
        related_scenarios = set()

        # Find all scenario bundles
        for s, p, o in self.oekg.triples((None, RDF.type, namespaces.OEO.OEO_00010252)):
            # find all scenarios in any bundle
            for s1, p1, o1 in self.oekg.triples(
                (s, namespaces.OEKG["has_scenario"], None)
            ):
                for s2, p2, o2_output_ds_uid in self.oekg.triples(
                    (o1, namespaces.OEO.RO_0002234, None)
                ):
                    if o2_output_ds_uid is not None:
                        for s3, p3, o3_input_ds_iri in oekg.triples(
                            (
                                o2_output_ds_uid,
                                namespaces.OEO["has_iri"],
                                Literal(table_iri),
                            )
                        ):
                            related_scenarios.add(s2)

        return related_scenarios

    def get_scenario_acronym(self, scenario_uri):
        """
        Currently not in use.
        Can be used to get the scenario acronym from scenario
        uid.
        """
        for s, p, o in self.oekg.triples((scenario_uri, namespaces.RDFS.label, None)):
            return o
