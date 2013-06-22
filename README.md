# Pylibsass

Pylibsass is a Python wrapper around the 
[libsass](https://github.com/hcatlin/libsass) library. The main goal of this
library is to provide an easy way to hook SASS compilation into your projects.

It uses the awesome [Watchdog](http://pythonhosted.org/watchdog/) library to
detect filesystem changes and recompile whenever there are changes detected.

```python
import pylibsass

pylibsass.watch("app/static/scss", "app/static/css")
```

## Installation

Installation is easy:

```sh
$ pip install pylibsass
```

## Development

Installing from source is easy. It is recommended to do this from within a 
virtualenv:

```sh
$ python setup.py develop
``` 

To run the tests, you do something similar:

```sh
$ python setup.py test
```

## Contributing

1. [Fork it!](https://help.github.com/articles/fork-a-repo)
1. Create your feature branch (`git checkout -b my-new-feature`)
1. Commit your changes (`git commit -am 'Added some feature'`)
1. Push to the branch (`git push origin my-new-feature`)
1. Create new Pull Request
