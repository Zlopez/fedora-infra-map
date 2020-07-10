# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""Test file for serializers/node_json_serializer.py file."""
import json
import uuid

from fedora_infra_map.serializers import node_json_serializer as ser
import fedora_infra_map.entities.node as node


def test_serialize_node():
    """
    Assert that serialization to JSON works.
    """
    code = uuid.uuid4()

    test_node = node.Node(
        code=code,
        name="node",
        description="description",
        issues_url="example.com/issues",
        sources_url="example.com/sources",
        homepage="example.com",
        prod_url="example.com",
        stg_url="stg.example.com",
        node_type=node.NodeType.OWNED_BY_CPE,
    )

    expected_json = """
        {{
            "code": "{}",
            "name": "node",
            "description": "description",
            "issues_url": "example.com/issues",
            "sources_url": "example.com/sources",
            "homepage": "example.com",
            "prod_url": "example.com",
            "stg_url": "stg.example.com",
            "node_type": {}
        }}
    """.format(
        code, node.NodeType.OWNED_BY_CPE.value
    )

    json_node = json.dumps(test_node, cls=ser.NodeJsonEncoder)

    assert json.loads(json_node) == json.loads(expected_json)
