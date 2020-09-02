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
""" Implementation of CSV database. """
import csv
from typing import Any, Sequence

from fedora_infra_map.entities.node import Node
from fedora_infra_map.entities.edge import Edge
from fedora_infra_map.database.database import Database


NODE_FIELDNAMES = [
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
EDGE_FIELDNAMES = [
    "code",
    "name",
    "description",
    "direction",
    "start_node",
    "end_node",
    "edge_type",
]


class CSVDatabase(Database):
    """
    Class implementing CSV database.
    This database is meant for testing purposes only,
    because it's slow and unreliable.

    Attributes:
      node_file: CSV file containing node objects
      edge_file: CSV file containing edge objects
    """

    def __init__(self, node_file: str, edge_file: str):
        """
        Initialize the CSVDatabase object.

        Arguments:
          node_file: Path to node file
          edge_file: Path to edge file
        """
        self.node_file = node_file
        self.edge_file = edge_file

    def list(self) -> Sequence[Any]:
        """
        List objects in the database.

        Returns:
          List of edges and nodes.
        """
        node_list = self._read_from_csv(self.node_file, NODE_FIELDNAMES)
        edge_list = self._read_from_csv(self.edge_file, EDGE_FIELDNAMES)

        node_objects = []
        for node in node_list:
            node["node_type"] = int(node["node_type"])
            node_objects.append(Node.from_dict(node))

        edge_objects = []
        for edge in edge_list:
            for node in node_list:
                if node["code"] == edge["start_node"]:
                    edge["start_node"] = node
                if node["code"] == edge["end_node"]:
                    edge["end_node"] = node

            edge["direction"] = int(edge["direction"])
            edge["edge_type"] = int(edge["edge_type"])
            edge_objects.append(Edge.from_dict(edge))

        return [*node_objects, *edge_objects]

    def _read_from_csv(self, file: str, fieldnames: Sequence[str]) -> Sequence[dict]:
        """
        Reads data from csv file with specified fieldnames.

        Returns:
          List of retrieved objects.
        """
        object_list = []
        with open(file, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames)
            for row in reader:
                object_list.append(row)

        return object_list
