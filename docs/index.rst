.. Pylibsass documentation master file, created by
   sphinx-quickstart on Thu Jun 27 18:51:38 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pylibsass: Python Wrapper around libsass
========================================

Release v\ |version|. (:ref:`Installation <install>`)

Pylibsass is a simple to use wrapper around the `libsass <https://github.com/hcatlin/libsass>`_ project.  It is released under the MIT license.

.. code-block:: python

    >>> import pylibsass
    >>> pylibsass.watch("app/static/scss", "app/static/css")

User Guide
----------

.. toctree::
    :maxdepth: 2

    user/install
    user/usage

API
---

.. toctree::
    :maxdepth: 2

    api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

