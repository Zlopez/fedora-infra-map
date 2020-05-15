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
"""Test file for entities/node.py file."""
import uuid

from fedora_infra_map.entities import node


def test_node_model_init():
    """
    Assert that the object is correctly initialized.
    """
    code = uuid.uuid4()
    test_node = node.Node(
        code,
        name="test",
        description="Test app",
        issues_url="example.com/issues",
        sources_url="example.com/sources",
        homepage="example.com",
        prod_url="example.com",
        stg_url="stg.example.com",
        node_type=node.NodeType.OWNED_BY_CPE,
    )

    assert test_node.code == code
    assert test_node.name == "test"
    assert test_node.description == "Test app"
    assert test_node.issues_url == "example.com/issues"
    assert test_node.sources_url == "example.com/sources"
    assert test_node.homepage == "example.com"
    assert test_node.prod_url == "example.com"
    assert test_node.stg_url == "stg.example.com"
    assert test_node.node_type == node.NodeType.OWNED_BY_CPE


def test_node_object_from_dict():
    """
    Assert that node object could be initialized from the dict.
    """
    code = uuid.uuid4()
    test_node = node.Node.from_dict(
        {
            "code": code,
            "name": "test",
            "description": "Test app",
            "issues_url": "example.com/issues",
            "sources_url": "example.com/sources",
            "homepage": "example.com",
            "prod_url": "example.com",
            "stg_url": "stg.example.com",
            "node_type": node.NodeType.OWNED_BY_CPE,
        }
    )

    assert test_node.code == code
    assert test_node.name == "test"
    assert test_node.description == "Test app"
    assert test_node.issues_url == "example.com/issues"
    assert test_node.sources_url == "example.com/sources"
    assert test_node.homepage == "example.com"
    assert test_node.prod_url == "example.com"
    assert test_node.stg_url == "stg.example.com"
    assert test_node.node_type == node.NodeType.OWNED_BY_CPE


def test_node_object_to_dict():
    """
    Assert that node object could be saved to dict.
    """
    code = uuid.uuid4()
    node_dict = {
        "code": code,
        "name": "test",
        "description": "Test app",
        "issues_url": "example.com/issues",
        "sources_url": "example.com/sources",
        "homepage": "example.com",
        "prod_url": "example.com",
        "stg_url": "stg.example.com",
        "node_type": node.NodeType.OWNED_BY_CPE,
    }

    test_node = node.Node.from_dict(node_dict)

    assert test_node.to_dict() == node_dict


def test_node_object_comparison():
    """
    Assert that comparison operator is working.
    """
    code = uuid.uuid4()
    node_dict = {
        "code": code,
        "name": "test",
        "description": "Test app",
        "issues_url": "example.com/issues",
        "sources_url": "example.com/sources",
        "homepage": "example.com",
        "prod_url": "example.com",
        "stg_url": "stg.example.com",
        "node_type": node.NodeType.OWNED_BY_CPE,
    }

    node1 = node.Node.from_dict(node_dict)
    node2 = node.Node.from_dict(node_dict)

    assert node1 == node2


def test_node_object_comparison_wrong_object():
    """
    Assert that comparison operator is failing with wrong type of object.
    """
    code = uuid.uuid4()
    node_dict = {
        "code": code,
        "name": "test",
        "description": "Test app",
        "issues_url": "example.com/issues",
        "sources_url": "example.com/sources",
        "homepage": "example.com",
        "prod_url": "example.com",
        "stg_url": "stg.example.com",
        "node_type": node.NodeType.OWNED_BY_CPE,
    }

    node1 = node.Node.from_dict(node_dict)

    assert node1 != {}
