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
"""Test file for serializers/edge_json_serializer.py file."""
import json
import uuid

from fedora_infra_map.serializers import edge_json_serializer as ser_edge
from fedora_infra_map.entities import edge, node

START_NODE = node.Node(
    uuid.uuid4(),
    name="Start node",
    description="Test app",
    issues_url="example.com/issues",
    sources_url="example.com/sources",
    homepage="example.com",
    prod_url="example.com",
    stg_url="stg.example.com",
    node_type=node.NodeType.OWNED_BY_CPE,
)
END_NODE = node.Node(
    uuid.uuid4(),
    name="End node",
    description="Test app",
    issues_url="example.com/issues",
    sources_url="example.com/sources",
    homepage="example.com",
    prod_url="example.com",
    stg_url="stg.example.com",
    node_type=node.NodeType.OWNED_BY_CPE,
)


def test_serialize_edge():
    """
    Assert that serialization to JSON works.
    """
    code = uuid.uuid4()

    test_edge = edge.Edge(
        code,
        name="test",
        description="Test relation",
        direction=edge.EdgeDirection.START_TO_END,
        start_node=START_NODE,
        end_node=END_NODE,
        edge_type=edge.EdgeType.FEDORA_MESSAGING,
    )

    expected_json = """
        {{
            "code": "{}",
            "name": "test",
            "description": "Test relation",
            "direction": {},
            "start_node": {{
                "code": "{}",
                "name": "Start node",
                "description": "Test app",
                "issues_url": "example.com/issues",
                "sources_url": "example.com/sources",
                "homepage": "example.com",
                "prod_url": "example.com",
                "stg_url": "stg.example.com",
                "node_type": {}
            }},
            "end_node": {{
                "code": "{}",
                "name": "End node",
                "description": "Test app",
                "issues_url": "example.com/issues",
                "sources_url": "example.com/sources",
                "homepage": "example.com",
                "prod_url": "example.com",
                "stg_url": "stg.example.com",
                "node_type": {}
            }},
            "edge_type": {}
        }}
    """.format(
        code,
        edge.EdgeDirection.START_TO_END.value,
        START_NODE.code,
        START_NODE.node_type.value,
        END_NODE.code,
        END_NODE.node_type.value,
        edge.EdgeType.FEDORA_MESSAGING.value,
    )

    json_edge = json.dumps(test_edge, cls=ser_edge.EdgeJsonEncoder)

    assert json.loads(json_edge) == json.loads(expected_json)


def test_serialize_edge_from_dict():
    """
    Assert that serialization to JSON works when object is created from dict.
    """
    code = uuid.uuid4()

    test_edge = edge.Edge.from_dict(
        {
            "code": code,
            "name": "test",
            "description": "Test relation",
            "direction": edge.EdgeDirection.START_TO_END.value,
            "start_node": START_NODE.to_dict(),
            "end_node": END_NODE.to_dict(),
            "edge_type": edge.EdgeType.FEDORA_MESSAGING.value,
        }
    )

    expected_json = """
        {{
            "code": "{}",
            "name": "test",
            "description": "Test relation",
            "direction": {},
            "start_node": {{
                "code": "{}",
                "name": "Start node",
                "description": "Test app",
                "issues_url": "example.com/issues",
                "sources_url": "example.com/sources",
                "homepage": "example.com",
                "prod_url": "example.com",
                "stg_url": "stg.example.com",
                "node_type": {}
            }},
            "end_node": {{
                "code": "{}",
                "name": "End node",
                "description": "Test app",
                "issues_url": "example.com/issues",
                "sources_url": "example.com/sources",
                "homepage": "example.com",
                "prod_url": "example.com",
                "stg_url": "stg.example.com",
                "node_type": {}
            }},
            "edge_type": {}
        }}
    """.format(
        code,
        edge.EdgeDirection.START_TO_END.value,
        START_NODE.code,
        START_NODE.node_type.value,
        END_NODE.code,
        END_NODE.node_type.value,
        edge.EdgeType.FEDORA_MESSAGING.value,
    )
    json_edge = json.dumps(test_edge, cls=ser_edge.EdgeJsonEncoder)

    assert json.loads(json_edge) == json.loads(expected_json)
