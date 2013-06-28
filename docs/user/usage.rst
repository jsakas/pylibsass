.. _usage:

Usage
=====
.. module:: pylibsass

This part of the documentation will give a high level overview of the different functions that pylibsass provides.

Libsass API
-----------

One of the goals of pylibsass if to provide a wrapper around the few functions that the libsass API provides. Currently, it only implements one of the functions, `compile()`::

    >>> import pylibsass.sass as sass
    >>> sass.compile(".test { color: red; }")

Not all of the exposed libsass API functions are exposed yet, but that is coming soon.

Helpers
-------

Since you probably don't want to be detecting changes to files, reading them, calling the `compile()` function, and then writing them out to a CSS file, pylibsass leverages the `Watchdog <http://pythonhosted.org/watchdog/>`_ library to handle that for you::

    >>> import pylibsass
    >>> pylibsass.watch("app/static/scss", "app/static/css")

Any changes in the source directory (`app/static/scss`) will be automatically compiled to the destination directory (`app/static/css`).
