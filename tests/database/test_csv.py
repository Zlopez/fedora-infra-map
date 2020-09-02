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
"""Test file for database/csv.py file."""
import csv
import uuid
import os

from fedora_infra_map.database import csv as fim_csv
from fedora_infra_map.entities.node import Node, NodeType
from fedora_infra_map.entities.edge import Edge, EdgeDirection, EdgeType


def test_list(tmpdir):
    """
    Assert that list of entities is returned.
    """
    code = uuid.uuid4()
    node_dict = {
        "code": str(code),
        "name": "test",
        "description": "Test app",
        "issues_url": "example.com/issues",
        "sources_url": "example.com/sources",
        "homepage": "example.com",
        "prod_url": "example.com",
        "stg_url": "stg.example.com",
        "node_type": NodeType.OWNED_BY_CPE.value,
    }
    code = uuid.uuid4()
    edge_dict = {
        "code": str(code),
        "name": "test",
        "description": "Test relation",
        "direction": EdgeDirection.START_TO_END.value,
        "start_node": node_dict,
        "end_node": node_dict,
        "edge_type": EdgeType.FEDORA_MESSAGING.value,
    }
    # Prepare csv files
    node_file = os.path.join(tmpdir, "node.csv")
    with open(node_file, "w", newline="") as csv_file:
        fieldnames = [
            "code",
            "name",
            "description",
            "issues_url",
            "sources_url",
            "homepage",
            "prod_url",
            "stg_url",
            "node_type",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(node_dict)
    edge_file = os.path.join(tmpdir, "edge.csv")
    with open(edge_file, "w", newline="") as csv_file:
        fieldnames = [
            "code",
            "name",
            "description",
            "direction",
            "start_node",
            "end_node",
            "edge_type",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_edge_dict = edge_dict.copy()
        csv_edge_dict["start_node"] = node_dict["code"]
        csv_edge_dict["end_node"] = node_dict["code"]
        writer.writerow(csv_edge_dict)

    db = fim_csv.CSVDatabase(node_file=node_file, edge_file=edge_file)

    entities = [Node.from_dict(node_dict), Edge.from_dict(edge_dict)]

    assert db.list() == entities
