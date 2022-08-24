import json

from omi.dialects.oep.dialect import OEP_V_1_4_Dialect, OEP_V_1_5_Dialect

from api import actions

from . import APITestCase


class TestPut(APITestCase):
    def setUp(self):
        structure_data = {
            "constraints": [
                {
                    "constraint_type": "PRIMARY KEY",
                    "constraint_parameter": "id",
                    "reference_table": None,
                    "reference_column": None,
                }
            ],
            "columns": [
                {
                    "name": "id",
                    "data_type": "bigserial",
                    "is_nullable": False,
                    "character_maximum_length": None,
                },
            ],
        }

        c_basic_resp = self.__class__.client.put(
            "/api/v0/schema/{schema}/tables/{table}/".format(
                schema=self.test_schema, table=self.test_table
            ),
            data=json.dumps({"query": structure_data}),
            HTTP_AUTHORIZATION="Token %s" % self.__class__.token,
            content_type="application/json",
        )

        assert c_basic_resp.status_code == 201, c_basic_resp.json().get(
            "reason", "No reason returned"
        )

    def tearDown(self):
        meta_schema = actions.get_meta_schema_name(self.test_schema)
        if actions.has_table(dict(table=self.test_table, schema=self.test_schema)):
            actions.perform_sql(
                "DROP TABLE IF EXISTS {schema}.{table} CASCADE".format(
                    schema=meta_schema,
                    table=actions.get_insert_table_name(
                        self.test_schema, self.test_table
                    ),
                )
            )
            actions.perform_sql(
                "DROP TABLE IF EXISTS {schema}.{table} CASCADE".format(
                    schema=meta_schema,
                    table=actions.get_edit_table_name(
                        self.test_schema, self.test_table
                    ),
                )
            )
            actions.perform_sql(
                "DROP TABLE IF EXISTS {schema}.{table} CASCADE".format(
                    schema=meta_schema,
                    table=actions.get_delete_table_name(
                        self.test_schema, self.test_table
                    ),
                )
            )
            actions.perform_sql(
                "DROP TABLE IF EXISTS {schema}.{table} CASCADE".format(
                    schema=self.test_schema, table=self.test_table
                )
            )

    def metadata_roundtrip(self, meta):
        response = self.__class__.client.post(
            "/api/v0/schema/{schema}/tables/{table}/meta/".format(
                schema=self.test_schema, table=self.test_table
            ),
            data=json.dumps(meta),
            HTTP_AUTHORIZATION="Token %s" % self.__class__.token,
            content_type="application/json",
        )

        self.assertEqual(
            response.status_code,
            200,
            response.content,
        )
        response = self.__class__.client.get(
            "/api/v0/schema/{schema}/tables/{table}/meta/".format(
                schema=self.test_schema, table=self.test_table
            )
        )

        self.assertEqual(response.status_code, 200, response.json())

        d_14 = (
            OEP_V_1_4_Dialect()
        )  # not tested anymore as OEM version is currently v1.5.1
        d_15 = OEP_V_1_5_Dialect()
        omi_meta = json.loads(json.dumps((d_15.compile(d_15.parse(json.dumps(meta))))))

        omi_meta_return = response.json()

        # ignore difference in keywords (by setting resulting keywords == input keywords)
        # REASON: the test re-uses the same test table, but does not delete the table tags in between
        # if we want to synchronize tagsand keywords, the roundtrip would otherwise fail
        omi_meta["keywords"] = omi_meta.get("keywords", [])
        omi_meta_return["keywords"] = omi_meta["keywords"]

        self.assertDictEqualKeywise(omi_meta_return, omi_meta)

    def test_nonexistent_key(self):
        meta = {"id": "id", "nonexistent_key": ""}
        response = self.__class__.client.post(
            "/api/v0/schema/{schema}/tables/{table}/meta/".format(
                schema=self.test_schema, table=self.test_table
            ),
            data=json.dumps(meta),
            HTTP_AUTHORIZATION="Token %s" % self.__class__.token,
            content_type="application/json",
        )

        # This should fail, but OMI does not warn about excess keys

        self.assertEqual(
            response.status_code,
            200,
            response.content,
        )

    def test_set_meta(self):
        meta = {"id": self.test_table}
        self.metadata_roundtrip(meta)

    def test_complete_metadata(self):
        null = None
        meta = {
            "name": "oep_metadata_table_example_v151",
            "title": "Example title for metadata example - Version 1.5.1",
            "id": "http://openenergyplatform.org/dataedit/view/model_draft/oep_metadata_table_example_v151",
            "description": "This is an metadata example for example data. There is a corresponding table on the OEP for each metadata version.",
            "language": ["en-GB", "en-US", "de-DE", "fr-FR"],
            "subject": [
                {
                    "name": "energy",
                    "path": "https://openenergy-platform.org/ontology/oeo/OEO_00000150",
                },
                {
                    "name": "test dataset",
                    "path": "https://openenergy-platform.org/ontology/oeo/OEO_00000408",
                },
            ],
            "keywords": ["energy", "example", "template", "test"],
            "publicationDate": "2022-02-15",
            "context": {
                "homepage": "https://reiner-lemoine-institut.de/lod-geoss/",
                "documentation": "https://openenergy-platform.org/tutorials/jupyter/OEMetadata/",
                "sourceCode": "https://github.com/OpenEnergyPlatform/oemetadata/tree/master",
                "contact": "https://github.com/Ludee",
                "grantNo": "03EI1005",
                "fundingAgency": "Bundesministerium für Wirtschaft und Klimaschutz",
                "fundingAgencyLogo": "https://commons.wikimedia.org/wiki/File:BMWi_Logo_2021.svg#/media/File:BMWi_Logo_2021.svg",
                "publisherLogo": "https://reiner-lemoine-institut.de//wp-content/uploads/2015/09/rlilogo.png",
            },
            "spatial": {"location": null, "extent": "europe", "resolution": "100 m"},
            "temporal": {
                "referenceDate": "2016-01-01",
                "timeseries": [
                    {
                        "start": "2017-01-01T00:00+01",
                        "end": "2017-12-31T23:00+01",
                        "resolution": "1 h",
                        "alignment": "left",
                        "aggregationType": "sum",
                    },
                    {
                        "start": "2018-01-01T00:00+01",
                        "end": "2019-06-01T23:00+01",
                        "resolution": "15 min",
                        "alignment": "right",
                        "aggregationType": "sum",
                    },
                ],
            },
            "sources": [
                {
                    "title": "OpenEnergyPlatform Metadata Example",
                    "description": "Metadata description",
                    "path": "https://github.com/OpenEnergyPlatform",
                    "licenses": [
                        {
                            "name": "CC0-1.0",
                            "title": "Creative Commons Zero v1.0 Universal",
                            "path": "https://creativecommons.org/publicdomain/zero/1.0/legalcode",
                            "instruction": "You are free: To Share, To Create, To Adapt",
                            "attribution": "© Reiner Lemoine Institut",
                        }
                    ],
                },
                {
                    "title": "OpenStreetMap",
                    "description": "A collaborative project to create a free editable map of the world",
                    "path": "https://www.openstreetmap.org/",
                    "licenses": [
                        {
                            "name": "ODbL-1.0",
                            "title": "Open Data Commons Open Database License 1.0",
                            "path": "https://opendatacommons.org/licenses/odbl/1.0/index.html",
                            "instruction": "You are free: To Share, To Create, To Adapt; As long as you: Attribute, Share-Alike, Keep open!",
                            "attribution": "© OpenStreetMap contributors",
                        }
                    ],
                },
            ],
            "licenses": [
                {
                    "name": "ODbL-1.0",
                    "title": "Open Data Commons Open Database License 1.0",
                    "path": "https://opendatacommons.org/licenses/odbl/1.0/",
                    "instruction": "You are free: To Share, To Create, To Adapt; As long as you: Attribute, Share-Alike, Keep open!",
                    "attribution": "© Reiner Lemoine Institut © OpenStreetMap contributors",
                }
            ],
            "contributors": [
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2016-06-16",
                    "object": "metadata",
                    "comment": "Create metadata",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2016-11-22",
                    "object": "metadata",
                    "comment": "Update metadata",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2016-11-22",
                    "object": "metadata",
                    "comment": "Update header and license",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-03-16",
                    "object": "metadata",
                    "comment": "Add license to source",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-03-28",
                    "object": "metadata",
                    "comment": "Add copyright to source and license",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-05-30",
                    "object": "metadata",
                    "comment": "Release metadata version 1.3",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-06-26",
                    "object": "metadata",
                    "comment": "Move referenceDate into temporal and remove array",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-07-19",
                    "object": "metadata",
                    "comment": "Start metadata version 1.4",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-07-26",
                    "object": "data",
                    "comment": "Rename table and files",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-10-18",
                    "object": "metadata",
                    "comment": "Add contribution object",
                },
                {
                    "title": "christian-rli",
                    "email": null,
                    "date": "2018-10-18",
                    "object": "metadata",
                    "comment": "Add datapackage compatibility",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-11-02",
                    "object": "metadata",
                    "comment": "Release metadata version 1.4",
                },
                {
                    "title": "christian-rli",
                    "email": null,
                    "date": "2019-02-05",
                    "object": "metadata",
                    "comment": "Apply template structure to example",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2019-03-22",
                    "object": "metadata",
                    "comment": "Hotfix foreignKeys",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2019-07-09",
                    "object": "metadata",
                    "comment": "Release metadata version OEP-1.3.0",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2021-11-15",
                    "object": "metadata",
                    "comment": "Release metadata version OEP-1.5.0",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2022-02-15",
                    "object": "metadata",
                    "comment": "Release metadata version OEP-1.5.1",
                },
            ],
            "resources": [
                {
                    "profile": "tabular-data-resource",
                    "name": "model_draft.oep_metadata_table_example_v151",
                    "path": "http://openenergyplatform.org/dataedit/view/model_draft/oep_metadata_table_example_v151",
                    "format": "PostgreSQL",
                    "encoding": "UTF-8",
                    "schema": {
                        "fields": [
                            {
                                "name": "id",
                                "description": "Unique identifier",
                                "type": "serial",
                                "unit": null,
                                "isAbout": [{"name": null, "path": null}],
                                "valueReference": [
                                    {"value": null, "name": null, "path": null}
                                ],
                            },
                            {
                                "name": "name",
                                "description": "Example name",
                                "type": "text",
                                "unit": null,
                                "isAbout": [
                                    {
                                        "name": "written name",
                                        "path": "https://openenergy-platform.org/ontology/oeo/IAO_0000590",
                                    }
                                ],
                                "valueReference": [
                                    {"value": null, "name": null, "path": null}
                                ],
                            },
                            {
                                "name": "type",
                                "description": "Type of wind farm",
                                "type": "text",
                                "unit": null,
                                "isAbout": [
                                    {
                                        "name": "wind farm",
                                        "path": "https://openenergy-platform.org/ontology/oeo/OEO_00000447",
                                    }
                                ],
                                "valueReference": [
                                    {
                                        "value": "onshore ",
                                        "name": "onshore wind farm",
                                        "path": "https://openenergy-platform.org/ontology/oeo/OEO_00000311",
                                    },
                                    {
                                        "value": "offshore ",
                                        "name": "offshore wind farm",
                                        "path": "https://openenergy-platform.org/ontology/oeo/OEO_00000308",
                                    },
                                ],
                            },
                            {
                                "name": "year",
                                "description": "Reference year",
                                "type": "integer",
                                "unit": null,
                                "isAbout": [
                                    {
                                        "name": "year",
                                        "path": "https://openenergy-platform.org/ontology/oeo/UO_0000036",
                                    }
                                ],
                                "valueReference": [
                                    {"value": null, "name": null, "path": null}
                                ],
                            },
                            {
                                "name": "value",
                                "description": "Example value",
                                "type": "double precision",
                                "unit": "MW",
                                "isAbout": [
                                    {
                                        "name": "quantity value",
                                        "path": "https://openenergy-platform.org/ontology/oeo/OEO_00000350",
                                    }
                                ],
                                "valueReference": [
                                    {"value": null, "name": null, "path": null}
                                ],
                            },
                            {
                                "name": "geom",
                                "description": "Geometry",
                                "type": "geometry(Point, 4326)",
                                "unit": null,
                                "isAbout": [
                                    {
                                        "name": "spatial region",
                                        "path": "https://openenergy-platform.org/ontology/oeo/BFO_0000006",
                                    }
                                ],
                                "valueReference": [
                                    {"value": null, "name": null, "path": null}
                                ],
                            },
                        ],
                        "primaryKey": ["id"],
                        "foreignKeys": [
                            {
                                "fields": ["year"],
                                "reference": {
                                    "resource": "schema.table",
                                    "fields": ["year"],
                                },
                            }
                        ],
                    },
                    "dialect": {"delimiter": null, "decimalSeparator": "."},
                }
            ],
            "@id": "https://databus.dbpedia.org/kurzum/mastr/bnetza-mastr/01.04.00",
            "@context": "https://github.com/OpenEnergyPlatform/oemetadata/blob/master/metadata/latest/context.json",
            "review": {
                "path": "https://github.com/OpenEnergyPlatform/data-preprocessing/issues",
                "badge": "Platinum",
            },
            "metaMetadata": {
                "metadataVersion": "OEP-1.5.1",
                "metadataLicense": {
                    "name": "CC0-1.0",
                    "title": "Creative Commons Zero v1.0 Universal",
                    "path": "https://creativecommons.org/publicdomain/zero/1.0/",
                },
            },
            "_comment": {
                "metadata": "Metadata documentation and explanation (https://github.com/OpenEnergyPlatform/oemetadata)",
                "dates": "Dates and time must follow the ISO8601 including time zone (YYYY-MM-DD or YYYY-MM-DDThh:mm:ss±hh)",
                "units": "Use a space between numbers and units (100 m)",
                "languages": "Languages must follow the IETF (BCP47) format (en-GB, en-US, de-DE)",
                "licenses": "License name must follow the SPDX License List (https://spdx.org/licenses/)",
                "review": "Following the OEP Data Review (https://github.com/OpenEnergyPlatform/data-preprocessing/blob/master/data-review/manual/review_manual.md)",
                "null": "If not applicable use: null",
                "todo": "If a value is not yet available, use: todo",
            },
        }
        meta_14 = {
            "name": "oep_metadata_table_example_v14",
            "title": "Good example title",
            "id": "https://openenergy-platform.org/dataedit/view/model_draft/oep_metadata_table_example_v14",
            "description": "example metadata for example data",
            "language": ["en-GB", "en-US", "de-DE", "fr-FR"],
            "keywords": ["example", "template", "test"],
            "publicationDate": "2018-06-12",
            "context": {
                "homepage": "https://reiner-lemoine-institut.de/szenariendb/",
                "documentation": "https://github.com/OpenEnergyPlatform/organisation/wiki/metadata",
                "sourceCode": "https://github.com/OpenEnergyPlatform/examples/tree/master/metadata",
                "contact": "https://github.com/Ludee",
                "grantNo": "03ET4057",
                "fundingAgency": "Bundesministerium für Wirtschaft und Energie",
                "fundingAgencyLogo": "https://www.innovation-beratung-foerderung.de/INNO/Redaktion/DE/Bilder/Titelbilder/titel_foerderlogo_bmwi.jpg?__blob=poster&v=2",
                "publisherLogo": "https://reiner-lemoine-institut.de//wp-content/uploads/2015/09/rlilogo.png",
            },
            "spatial": {"location": null, "extent": "europe", "resolution": "100 m"},
            "temporal": {
                "referenceDate": "2016-01-01",
                "timeseries": {
                    "start": "2017-01-01T00:00+01",
                    "end": "2017-12-31T23:00+01",
                    "resolution": "1 h",
                    "alignment": "left",
                    "aggregationType": "sum",
                },
            },
            "sources": [
                {
                    "title": "OpenEnergyPlatform Metadata Example",
                    "description": "Metadata description",
                    "path": "https://github.com/OpenEnergyPlatform",
                    "licenses": [
                        {
                            "name": "CC0-1.0",
                            "title": "Creative Commons Zero v1.0 Universal",
                            "path": "https://creativecommons.org/publicdomain/zero/1.0/legalcode",
                            "instruction": "You are free: To Share, To Create, To Adapt",
                            "attribution": "© Reiner Lemoine Institut",
                        }
                    ],
                },
                {
                    "title": "OpenStreetMap",
                    "description": "A collaborative project to create a free editable map of the world",
                    "path": "https://www.openstreetmap.org/",
                    "licenses": [
                        {
                            "name": "ODbL-1.0",
                            "title": "Open Data Commons Open Database License 1.0",
                            "path": "https://opendatacommons.org/licenses/odbl/1.0/",
                            "instruction": "You are free: To Share, To Create, To Adapt; As long as you: Attribute, Share-Alike, Keep open!",
                            "attribution": "© OpenStreetMap contributors",
                        }
                    ],
                },
            ],
            "licenses": [
                {
                    "name": "ODbL-1.0",
                    "title": "Open Data Commons Open Database License 1.0",
                    "path": "https://opendatacommons.org/licenses/odbl/1.0/",
                    "instruction": "You are free: To Share, To Create, To Adapt; As long as you: Attribute, Share-Alike, Keep open!",
                    "attribution": "© Reiner Lemoine Institut © OpenStreetMap contributors",
                }
            ],
            "contributors": [
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2016-06-16",
                    "object": "metadata",
                    "comment": "Create metadata",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2016-11-22",
                    "object": "metadata",
                    "comment": "Update metadata",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2016-11-22",
                    "object": "metadata",
                    "comment": "Update header and license",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-03-16",
                    "object": "metadata",
                    "comment": "Add license to source",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-03-28",
                    "object": "metadata",
                    "comment": "Add copyright to source and license",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-05-30",
                    "object": "metadata",
                    "comment": "Release metadata version 1.3",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2017-06-26",
                    "object": "metadata",
                    "comment": "Move referenceDate into temporal and remove array",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-07-19",
                    "object": "metadata",
                    "comment": "Start metadata version 1.4",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-07-26",
                    "object": "data",
                    "comment": "Rename table and files",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-10-18",
                    "object": "metadata",
                    "comment": "Add contribution object",
                },
                {
                    "title": "christian-rli",
                    "email": null,
                    "date": "2018-10-18",
                    "object": "metadata",
                    "comment": "Add datapackage compatibility",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2018-11-02",
                    "object": "metadata",
                    "comment": "Release metadata version 1.4",
                },
                {
                    "title": "christian-rli",
                    "email": null,
                    "date": "2019-02-05",
                    "object": "metadata",
                    "comment": "Apply template structure to example",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2019-03-22",
                    "object": "metadata",
                    "comment": "Hotfix foreignKeys",
                },
                {
                    "title": "Ludee",
                    "email": null,
                    "date": "2019-07-09",
                    "object": "metadata",
                    "comment": "Release metadata version OEP-1.3.0",
                },
            ],
            "resources": [
                {
                    "profile": "tabular-data-resource",
                    "name": "model_draft.oep_metadata_table_example_v14",
                    "path": "https://openenergy-platform.org/dataedit/view/model_draft/oep_metadata_table_example_v14",
                    "format": "PostgreSQL",
                    "encoding": "UTF-8",
                    "schema": {
                        "fields": [
                            {
                                "name": "id",
                                "description": "Unique identifier",
                                "type": "serial",
                                "unit": null,
                            },
                            {
                                "name": "year",
                                "description": "Reference year",
                                "type": "integer",
                                "unit": null,
                            },
                            {
                                "name": "value",
                                "description": "Example value",
                                "type": "double precision",
                                "unit": "MW",
                            },
                            {
                                "name": "geom",
                                "description": "Geometry",
                                "type": "geometry(Point, 4326)",
                                "unit": null,
                            },
                        ],
                        "primaryKey": ["id"],
                        "foreignKeys": [
                            {
                                "fields": ["year"],
                                "reference": {
                                    "resource": "schema.table",
                                    "fields": ["year"],
                                },
                            }
                        ],
                    },
                    "dialect": {"delimiter": null, "decimalSeparator": "."},
                }
            ],
            "review": {
                "path": "https://github.com/OpenEnergyPlatform/data-preprocessing/wiki",
                "badge": "platin",
            },
            "metaMetadata": {
                "metadataVersion": "OEP-1.4.0",
                "metadataLicense": {
                    "name": "CC0-1.0",
                    "title": "Creative Commons Zero v1.0 Universal",
                    "path": "https://creativecommons.org/publicdomain/zero/1.0/",
                },
            },
            "_comment": {
                "metadata": "Metadata documentation and explanation (https://github.com/OpenEnergyPlatform/organisation/wiki/metadata)",
                "dates": "Dates and time must follow the ISO8601 including time zone (YYYY-MM-DD or YYYY-MM-DDThh:mm:ss±hh)",
                "units": "Use a space between numbers and units (100 m)",
                "languages": "Languages must follow the IETF (BCP47) format (en-GB, en-US, de-DE)",
                "licenses": "License name must follow the SPDX License List (https://spdx.org/licenses/)",
                "review": "Following the OEP Data Review (https://github.com/OpenEnergyPlatform/data-preprocessing/wiki)",
                "null": "If not applicable use (null)",
            },
        }

        self.metadata_roundtrip(meta)
