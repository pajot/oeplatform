import json

import requests

from api.tests import APITestCaseWithTable

from ..util import load_content_as_json


class TestAliasesTracking(APITestCaseWithTable):
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
            {
                "name": "name",
                "data_type": "character varying",
                "is_nullable": True,
                "character_maximum_length": 123,
            },
        ],
    }

    data = [{"name": "Hans"}, {"name": "Petra"}]

    def test_aliases_in_form_clauses(self):
        data = {
            "query": {
                "fields": [dict(type="column", column="id", table="a")],
                "where": [
                    {
                        "type": "operator",
                        "operator": "=",
                        "operands": [
                            {"type": "column", "column": "name", "table": "a"},
                            {"type": "value", "value": "Hans"},
                        ],
                    }
                ],
                "from": {
                    "type": "join",
                    "left": {
                        "type": "table",
                        "table": self.test_table,
                        "schema": self.test_schema,
                        "alias": "a",
                    },
                    "right": {
                        "type": "table",
                        "table": self.test_table,
                        "schema": self.test_schema,
                        "alias": "b",
                    },
                    "on": [
                        {
                            "type": "operator",
                            "operator": "=",
                            "operands": [
                                {"type": "column", "column": "id", "table": "a"},
                                {"type": "column", "column": "id", "table": "b"},
                            ],
                        }
                    ],
                },
            }
        }

        self.check_api_post("/api/v0/advanced/search", data=data, expected_result=[[1]])
