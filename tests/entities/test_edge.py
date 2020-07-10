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
"""Test file for entities/edge.py file."""
import uuid
from unittest import mock

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


def test_edge_model_init():
    """
    Assert that the object is correctly initialized.
    """
    code = uuid.uuid4()
    start_node = mock.Mock()
    end_node = mock.Mock()
    test_edge = edge.Edge(
        code,
        name="test",
        description="Test relation",
        direction=edge.EdgeDirection.START_TO_END,
        start_node=start_node,
        end_node=end_node,
        edge_type=edge.EdgeType.FEDORA_MESSAGING,
    )

    assert test_edge.code == code
    assert test_edge.name == "test"
    assert test_edge.description == "Test relation"
    assert test_edge.direction == edge.EdgeDirection.START_TO_END
    assert test_edge.start_node == start_node
    assert test_edge.end_node == end_node
    assert test_edge.edge_type == edge.EdgeType.FEDORA_MESSAGING


def test_edge_object_from_dict():
    """
    Assert that edge object could be initialized from the dict.
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

    assert test_edge.code == code
    assert test_edge.name == "test"
    assert test_edge.description == "Test relation"
    assert test_edge.direction == edge.EdgeDirection.START_TO_END
    assert test_edge.start_node == START_NODE
    assert test_edge.end_node == END_NODE
    assert test_edge.edge_type == edge.EdgeType.FEDORA_MESSAGING


def test_edge_object_to_dict():
    """
    Assert that edge object could be saved to dict.
    """
    code = uuid.uuid4()
    edge_dict = {
        "code": code,
        "name": "test",
        "description": "Test relation",
        "direction": edge.EdgeDirection.START_TO_END.value,
        "start_node": START_NODE.to_dict(),
        "end_node": END_NODE.to_dict(),
        "edge_type": edge.EdgeType.FEDORA_MESSAGING.value,
    }

    test_edge = edge.Edge.from_dict(edge_dict)

    assert test_edge.to_dict() == edge_dict


def test_edge_object_comparison():
    """
    Assert that comparison operator is working.
    """
    code = uuid.uuid4()
    edge_dict = {
        "code": code,
        "name": "test",
        "description": "Test relation",
        "direction": edge.EdgeDirection.START_TO_END,
        "start_node": START_NODE.to_dict(),
        "end_node": END_NODE.to_dict(),
        "edge_type": edge.EdgeType.FEDORA_MESSAGING,
    }

    edge1 = edge.Edge.from_dict(edge_dict)
    edge2 = edge.Edge.from_dict(edge_dict)

    assert edge1 == edge2


def test_edge_object_comparison_wrong_object():
    """
    Assert that comparison operator is failing with wrong type of object.
    """
    code = uuid.uuid4()
    edge_dict = {
        "code": code,
        "name": "test",
        "description": "Test relation",
        "direction": edge.EdgeDirection.START_TO_END,
        "start_node": START_NODE.to_dict(),
        "end_node": END_NODE.to_dict(),
        "edge_type": edge.EdgeType.FEDORA_MESSAGING,
    }

    edge1 = edge.Edge.from_dict(edge_dict)

    assert edge1 != {}
