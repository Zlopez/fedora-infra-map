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
"""Definition of node entity."""
from __future__ import annotations
from enum import Enum

from fedora_infra_map.entities.node import Node


class EdgeType(Enum):
    """
    Enum for edge types.

    FEDORA_MESSAGING: Fedora messaging communication
    API: Communication over API
    HTTP: Communication over HTTP/S protocol
    XML: Communication over XML RPC
    """

    FEDORA_MESSAGING = 0
    API = 1
    HTTP = 2
    XML = 3


class EdgeDirection(Enum):
    """
    Enum for edge direction.

    START_TO_END: Relation between nodes is one directional from start node to end node
    END_TO_START: Relation between nodes is one directional from end node to start node
    BOTH: Relation between nodes is bi-directional
    """

    START_TO_END = 0
    END_TO_START = 1
    BOTH = 2


class Edge:
    """
    Class that represents relation edge between two nodes in graph.

    Attributes:
        code: Unique identifier
        name: Name of the relation
        description: Brief description of the relation
        direction: Direction of the relation
        start_node: First node in the relation
        end_node: Second node in the relation
        edge_type: Type of the relation/communication
    """

    def __init__(
        self,
        code: str,
        name: str,
        description: str,
        direction: EdgeDirection,
        start_node: Node,
        end_node: Node,
        edge_type: EdgeType,
    ) -> None:
        """
        Class constructor
        """
        self.code = code
        self.name = name
        self.description = description
        self.direction = direction
        self.start_node = start_node
        self.end_node = end_node
        self.edge_type = edge_type

    @classmethod
    def from_dict(cls, adict: dict) -> Edge:
        """
        Create object from dictionary.

        Params:
            adict: Input dictionary

        Returns:
            Object instance.
        """
        return cls(
            code=adict["code"],
            name=adict["name"],
            description=adict["description"],
            direction=adict["direction"],
            start_node=adict["start_node"],
            end_node=adict["end_node"],
            edge_type=adict["edge_type"],
        )

    def to_dict(self) -> dict:
        """
        Create dictionary from object.

        Returns:
            Dictionary representing object.
        """
        return {
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "direction": self.direction,
            "start_node": self.start_node,
            "end_node": self.end_node,
            "edge_type": self.edge_type,
        }

    def __eq__(self, other: object) -> bool:
        """
        Comparison operator.

        Return:
            Compare output.
        """
        if not isinstance(other, Edge):
            return NotImplemented
        return self.to_dict() == other.to_dict()
