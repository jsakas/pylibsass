.. _api:

Pylibsass API
=============

.. module:: pylibsass

This section of the documentation provides an introduction to all of the pylibsass interface. All of the important stuff should be here. If there is something missing, the source code is available on `GitHub <https://github.com/rsenk330/pylibsass`.

Main Interface
--------------

The major functions will be exposed directly through the main `pylibsass` package.

.. autofunction:: watch

Lower-Level Interface
---------------------

The lower-level interface is used by the main interface. If you need to do something weird, these functions will be useful. These typically interact directly with libsass.

.. autofunction:: pylibsass.sass.compile_str
.. autoclass:: pylibsass.sass.LibSass
    :inherited-members:

C Structs
---------

The C structs are ctypes definitions for the libsass structs. See the `libsass project documentation <https://github.com/hcatlin/libsass>`_ for more information.

.. autoclass:: pylibsass.sass.SassContext
    :inherited-members:
.. autoclass:: pylibsass.sass.SassFileContext
    :inherited-members:
.. autoclass:: pylibsass.sass.SassFolderContext
    :inherited-members:
