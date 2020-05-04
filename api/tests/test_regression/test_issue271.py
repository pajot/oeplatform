import json

import requests

from api.tests import APITestCaseWithTable

from ..util import load_content_as_json


class Test271(APITestCaseWithTable):

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

    def test_271(self):
        data = {
            "query": {
                "fields": [dict(type="column", column="name")],
                "where": [
                    {
                        "type": "operator",
                        "operator": "=",
                        "operands": [
                            {"type": "column", "column": "name"},
                            {"type": "value", "value": "Hans"},
                        ],
                    }
                ],
                "from": {
                    "type": "table",
                    "table": self.test_table,
                    "schema": self.test_schema,
                },
            }
        }

        self.check_api_post(
            "/api/v0/advanced/search", data=data, expected_result=[["Hans"]]
        )

    def test_271_column_does_not_exist(self):
        data = {
            "query": {
                "fields": [dict(type="column", column="does_not_exist")],
                "from": {
                    "type": "table",
                    "table": self.test_table,
                    "schema": self.test_schema,
                },
            }
        }
        resp = self.__class__.client.post(
            "/api/v0/advanced/search",
            data=json.dumps(data),
            HTTP_AUTHORIZATION="Token %s" % self.__class__.token,
            content_type="application/json",
        )

        self.assertEqual(
            resp.status_code, 400, resp.json().get("reason", "No reason returned")
        )

        json_resp = resp.json()

        self.assertEqual(json_resp["reason"], 'column "does_not_exist" does not exist')
