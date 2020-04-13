======
alscli
======

Toolset for Ableton Live Set (als) files

Recipes
=======

Find used plugins in all projects

.. code-block:: bash
    find . -name '*.als' -exec bash -c 'echo "{}"; alscli list-plugins "{}"' \; | tee ~/work/sandbox/plugins.txt

* Free software: MIT license
