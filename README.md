# Flaskage #
*A complete and carefully designed template for use with the Flask web framework*

[![Build Status](https://travis-ci.org/fgimian/flaskage.png?branch=master)](https://travis-ci.org/fgimian/flaskage)

![Flaskage Logo](https://raw.githubusercontent.com/fgimian/flaskage/master/docs/_static/flaskage-full.png)

Awesome artwork provided courtesy of [Open Clip Art Library](http://openclipart.org/detail/168585/knight-sheep-by-dodger2)

## Documentation ##

Please check out the [Flaskage documentation at Read the Docs](http://flaskage.readthedocs.org/).

## Quick Start ##

Install Flaskage in your virtualenv as follows:

``` bash
pip install git+git://github.com/fgimian/flaskage.git
```

Create a new project:

``` bash
flaskage new <project-name>
```

Start the development server and check out your new project:

``` bash
cd <project-name>
./manage.py server
```

Refer to the [documentation](http://flaskage.readthedocs.org/) for further instruction.

## TODO ##

Flaskage is currently a work in progress.  My current outstanding tasks are:

* Improve the way colors are adjusted when using the flaskage command
* Consider requirements files for each environment
* Provide the ability to turn off colors when using the flaskage command
* Improve organisation of assets and resolve multiple registrations during
  testing
* Determine the best way to deal with symbolic link for Twitter Bootstrap fonts
* Consider a better way to store sensitive configuration (e.g. secret keys
  and database credentials)
* Create a scaffolding command for helpers
* Consider a scaffolding command for BDD and Jade templates
* Complete writing documentation
* Complete unit tests for the flaskage CLI tool

Long-term goals are as follows:

* Generation of scaffolding including CRUD
* Pluggable scaffolding modules
* Ability to generate foreign keys and relationships via scaffolding
