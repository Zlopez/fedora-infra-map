===========================
Fedora Infra Map app design
===========================

Fedora Infra Map is using clean architecture design and directories structure based on the requirements. Clean architecture was chosen to allow Fedora Infra Map parts to be easily replaceable and easily maintainable.

The design will be split to three parts relevant to three layers Entities, Use Cases and External systems.

Entities
--------

Inner definitions of objects we will work with. This is the core of the whole application. Bellow is the directory structure.

::
   Entities
   + init.py
   + node.py
   + edge.py

node.py
~~~~~~~

Internal representation of node in the map.

edge.py
~~~~~~~

Internal representation of edge in the map.
