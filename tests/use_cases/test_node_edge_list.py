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
"""Test file for use_cases/node_edge_list.py file."""
import pytest
import uuid
from unittest import mock

from fedora_infra_map.entities import edge, node
from fedora_infra_map.use_cases import node_edge_list as uc


@pytest.fixture
def entities_edge_node():
    """
    Fixture to return fake list of edges and nodes.
    """

    start_node = node.Node(
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
    end_node = node.Node(
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

    isolated_node = node.Node(
        uuid.uuid4(),
        name="Isolated node",
        description="Test app",
        issues_url="example.com/issues",
        sources_url="example.com/sources",
        homepage="example.com",
        prod_url="example.com",
        stg_url="stg.example.com",
        node_type=node.NodeType.OWNED_BY_CPE,
    )

    test_edge = edge.Edge(
        uuid.uuid4(),
        name="test",
        description="Test relation",
        direction=edge.EdgeDirection.START_TO_END,
        start_node=start_node,
        end_node=end_node,
        edge_type=edge.EdgeType.FEDORA_MESSAGING,
    )

    return [test_edge, isolated_node]


def test_node_edge_list_without_parameters(entities_edge_node):
    """
    Assert that correct list is retrieved.
    """
    db = mock.Mock()
    db.list.return_value = entities_edge_node

    edge_node_list_use_case = uc.NodeEdgeListUseCase(db)
    result = edge_node_list_use_case.execute()

    db.list.assert_called_with()
    assert result == entities_edge_node
