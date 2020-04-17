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


class NodeType(Enum):
    """
    Enum for node types. The types are defined by the ownership of the apps by CPE team.
    """

    OWNED_BY_CPE = 0
    HOSTED_BY_CPE = 1
    NOT_HOSTED_OR_OWNED_BY_CPE = 2


class Node:
    """
    Class that represents application node in graph.

    Attributes:
        code: Unique identifier
        name: Name of the app
        description: Brief description of the app
        issues_url: URL to issue tracker
        sources_url: URL to application sources
        homepage: Homepage of the app
        prod_url: Production URL where the app is running
        stg_url: URL of staging/testing instance of the app
        node_type: Type of the node
    """

    def __init__(
        self,
        code: str,
        name: str,
        description: str,
        issues_url: str,
        sources_url: str,
        homepage: str,
        prod_url: str,
        stg_url: str,
        node_type: NodeType,
    ) -> None:
        """
        Class constructor
        """
        self.code = code
        self.name = name
        self.description = description
        self.issues_url = issues_url
        self.sources_url = sources_url
        self.homepage = homepage
        self.prod_url = prod_url
        self.stg_url = stg_url
        self.node_type = node_type

    @classmethod
    def from_dict(cls, adict: dict) -> Node:
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
            issues_url=adict["issues_url"],
            sources_url=adict["sources_url"],
            homepage=adict["homepage"],
            prod_url=adict["prod_url"],
            stg_url=adict["stg_url"],
            node_type=adict["node_type"],
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
            "issues_url": self.issues_url,
            "sources_url": self.sources_url,
            "homepage": self.homepage,
            "prod_url": self.prod_url,
            "stg_url": self.stg_url,
            "node_type": self.node_type,
        }

    def __eq__(self, other: Node) -> bool:
        """
        Comparison operator.

        Return:
            Compare output.
        """
        return self.to_dict() == other.to_dict()
