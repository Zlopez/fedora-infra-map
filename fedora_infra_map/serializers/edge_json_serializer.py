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
"""JSON serializer for `entities.edge.Edge` class."""

import json

from fedora_infra_map.serializers import node_json_serializer as ser


class EdgeJsonEncoder(json.JSONEncoder):
    """
    JSON encoder for `entities.edge.Edge` class.
    """

    def default(self, o):
        try:
            to_serialize = {
                "code": str(o.code),
                "name": o.name,
                "description": o.description,
                "direction": o.direction.value,
                # This looks insane, but we need to convert the Node to JSON string
                # and then get basic dict from it
                "start_node": json.loads(
                    json.dumps(o.start_node, cls=ser.NodeJsonEncoder)
                ),
                "end_node": json.loads(json.dumps(o.end_node, cls=ser.NodeJsonEncoder)),
                "edge_type": o.edge_type.value,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
