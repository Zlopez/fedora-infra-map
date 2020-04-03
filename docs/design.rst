===========================
Fedora Infra Map app design
===========================

Fedora Infra Map is using clean architecture design and directories structure based on the requirements. Clean architecture was chosen to allow Fedora Infra Map parts to be easily replaceable and easily maintainable.

The design will be split to three parts relevant to three layers Entities, Use Cases and External systems.

Entities
--------

Inner definitions of objects we will work with and their serializers. This is the core of the whole application. Bellow is the directory structure.

::

  fedora_infra_map
  +-- entities
    +-- init.py
    +-- node.py
    +-- edge.py
  +-- serializers
    +-- init.py
    +-- node_json_serializer.py
    +-- edge_json_serializer.py


node.py
~~~~~~~

Internal representation of node in the map. One node = one app.


edge.py
~~~~~~~

Internal representation of edge in the map. One edge = one relationship between two apps.


node_json_serializer
~~~~~~~~~~~~~~~~~~~~

JSON serializer for node object. This allows us to use `json.dumps` on the `Node` object.


edge_json_serializer
~~~~~~~~~~~~~~~~~~~~

JSON serializer for edge object. This allows us to use `json.dumps` on the `Edge` object.


Use cases
---------

Use cases corresponds to requirements. This layer will define what the application can do. Bellow is the directory structure for this layer. This layer also contains abstract classes which will be inherited by external systems and response/requests definition with any exceptions.

::

  fedora_infra_map
  +-- use_cases
    +-- init.py
    +-- node_edge_list.py
  +-- request_objects
    +-- init.py
    +-- node_edge_list_request.py
  +-- response_objects
    +-- init.py
    +-- response.py
    +-- response_success.py
    +-- response_failure.py
  +-- database
    +-- init.py
    +-- database.py


node_edge_list
~~~~~~~~~~~~~~

This class returns the list of nodes and list of edges connecting them or error. It calls abstract `Database` class, request a query and handle response from external system.


node_edge_list_request
~~~~~~~~~~~~~~~~~~~~~~

Request passed to `node_edge_list` it contains a list of filters to apply.


response
~~~~~~~~

Abstract class which is inherited by other responses. This class also defines constants for any response code. Defines `__bool__` method.


response_success
~~~~~~~~~~~~~~~~

This class is inherited from `Response` and is returned when use case finishes successfully. Implements `__bool__` method that returns `True` and value attribute, which contains return value from use case if any.


response_failure
~~~~~~~~~~~~~~~~

This class is inherited from `Response` and is returned when use case finishes with failure. Implements `__bool__` method that returns `False`, value property contains type of error and exception with error message.


database
~~~~~~~~

Abstract class that defines the API for database. It needs to be inherited by any external database class.


External systems
----------------

This is the outer layer of clean architecture and contains wrappers that are calling external systems and any helper class used by the wrappers. Wrappers will inherit abstract class defined in use cases layer.

::

  fedora_infra_map
  +-- database
    +-- csv.py


csv
~~~

This class implements database wrapper around CSV files.
